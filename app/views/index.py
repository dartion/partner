#  partner -   index.py
#  Description:
#  Author:           darshan
#  Created:          21 Dec. 2019
#  Source:           https://github.com/dartion/partner
#  License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential

#  partner - login.py
#
#

#  partner - login.py
#
#


from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms.user.login import UserLoginForm
from app.forms.user.register import UserRegisterForm
from app.forms.user.forgot_password import  ForgotPasswordForm
from app.forms.user.reset_password import  ResetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib.auth.models import User
from app.models import ResetPassword, ProfileBasicInfo
import json

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username_from_form = form.cleaned_data.get('Username')
        password_from_form = form.cleaned_data.get('Password')
        user = authenticate(username=username_from_form, password=password_from_form)


        if username_from_form is None or password_from_form is None:
            context = {
                'form': form
            }
            return render(request, "login/login.html", context)

        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, "login/login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        # Commit = False will not save the form unless save() method is called
        user = form.save(commit=False)
        print(form.cleaned_data.get('password'))
        password = form.cleaned_data.get('password')
        user.is_active=False
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        # login(request, new_user)
        if next:
            return redirect(next)
        messages.add_message(request, messages.SUCCESS, "{} user has been registered successfully. Please wait until the administrator approves your account".format(user.username))

        subject = 'New User Request'

        message = ''
        html_message = render_to_string('user/new_user_email_template.html', {
                                         'url': "{}".format(settings.ALLOWED_HOSTS[0]
                                                            )})
        email_from = settings.EMAIL_SENDER
        recipient_list = [settings.ADMIN_EMAIL]
        send_mail(subject, message, from_email=email_from, recipient_list=recipient_list, html_message=html_message)
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, "login/register.html", context)


def logout_view(request):

    messages.add_message(request, messages.WARNING, "User successfully logged out")
    logout(request)
    return redirect('/')


@login_required
def home(request):
    profile_list = []
    admin = False
    if request.user.is_superuser:
        profile_list = ProfileBasicInfo.objects.all()
        context = {'profile_list': profile_list, 'userID': int(request.user.id)}
    else:
        profile_list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
        context = {'profile_list': profile_list, 'userID': int(request.user.id)}
    if request.user.is_superuser:
        admin = True
    context = {'profile_list': profile_list, 'userID': int(request.user.id), "admin_user":admin}
    return render(request, "user/index.html", context=context)


def forgot_password(request):
    form = ForgotPasswordForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "A reset password link has been sent to your registered email. Please click on the link to reset the password.")

        return redirect('/')
    return render(request, "forgot_password/forgot_password_page.html", context)


def reset_password(request, id, reset_number):
    try:
        user = User.objects.get(id=id)
    except Exception as ex:
        messages.add_message(request, messages.ERROR,
                             "User does not exist in the system. Please contact administrator")
        return redirect('/')

    try:
        match_reset_number =  ResetPassword.objects.get(reset_password_number=reset_number)
    except Exception as ex:
        messages.add_message(request, messages.ERROR,
                             "Unique Reset Password ID cannot be found, try resetting your password again.")
        return redirect('/')

    form = ResetPasswordForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save(user)
        messages.add_message(request, messages.SUCCESS,
                             "Password for user {} has been successfully updated".format(user.username))
        return redirect('/')
    return render(request, "forgot_password/reset_password.html", context)


@login_required
def ajax_get_profile_list(request,user_id):

    user = User.objects.get(id=user_id)
    profile_list = []
    if user.is_superuser:
        profile_list_objects = ProfileBasicInfo.objects.all()
    else:
        profile_list_objects = ProfileBasicInfo.objects.filter(user_id=user_id)

    for i in profile_list_objects:
        print(i.first_name)

    for i in profile_list_objects:
        profile_list_dict = {}
        profile_list_dict['first_name'] = i.first_name  + " " + i.last_name
        profile_list_dict['dob'] = str(i.dob)
        profile_list_dict['phone_number'] = i.phone_number
        profile_list_dict['id'] = i.id
        profile_list_dict['submit'] = i.submit
        profile_list_dict['message'] = False
        profile_list_dict['is_active'] = i.is_active

        if request.user.is_superuser:
            profile_list_dict['is_active'] = i.is_active
        profile_list.append(profile_list_dict)

    retVal = {"data": profile_list}
    print(retVal)
    return HttpResponse(json.dumps(retVal), content_type="application/json")


def about_us(request):
    return render(request, "menu_content/about_us.html")


def how_to_start(request):
    return render(request, "menu_content/how_to_start.html")


# def home_page(request):
#     return render(request, "menu_content/home_page.html")


def search_profiles(request):


    return render(request, "menu_content/search_profiles.html")

def contact_us(request):
    return render(request, "menu_content/contact_us.html")


@login_required
def activate_profile_owner(request, id):
    try:
        if request.user.is_superuser:
            user = User.objects.get(id=id)
            user.is_active = True
            user.save()
            subject = '{} - User Activated'.format(user.first_name)

            message = ''
            html_message = render_to_string('user/user_activated_email_template.html', {
                'url': "{}".format(settings.ALLOWED_HOSTS[0]), 'user': user.first_name})
            email_from = settings.EMAIL_SENDER
            recipient_list = [user.email]
            send_mail(subject, message, from_email=email_from, recipient_list=recipient_list, html_message=html_message)


            messages.add_message(request, messages.SUCCESS,
                                 "User has been activated successfully.")
            return redirect('/user_list')

    except Exception as ex:

        messages.add_message(request, messages.ERROR,
                             "You are not allowed to activate a user.")
        return redirect('/')


@login_required
def deactivate_profile_owner(request, id):
    try:
        if request.user.is_superuser:
            user = User.objects.get(id=id)
            user.is_active = False
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 "User has been deactivated successfully.")
            subject = '{} - User Deactivated'.format(user.first_name)

            message = ''
            html_message = render_to_string('user/user_deactivated_email_template.html', {
                'url': "{}".format(settings.ALLOWED_HOSTS[0])
                                   , 'user': user.first_name })
            email_from = settings.EMAIL_SENDER
            recipient_list = [user.email]
            send_mail(subject, message, from_email=email_from, recipient_list=recipient_list, html_message=html_message)

            return redirect('/user_list')

    except Exception as ex:

        messages.add_message(request, messages.ERROR,
                             "You are not allowed to activate a user.")
        return redirect('/')

@login_required
def ajax_get_user_list(request):
    try:
        if request.user.is_superuser:
            user_list = []
            all_users = User.objects.all()

            for i in all_users:
                profile_list_dict = {}
                profile_list_dict['id'] = i.id
                profile_list_dict['name'] = i.first_name + " " + i.last_name
                profile_list_dict['username'] = str(i.username)
                profile_list_dict['email'] = str(i.email)
                profile_list_dict['is_active'] = i.is_active

                user_list.append(profile_list_dict)

            retVal = {"data": user_list}
            print(retVal)
            return HttpResponse(json.dumps(retVal), content_type="application/json")
    except Exception as ex:
        return redirect('/')

@login_required
def user_list(request):
    if request.user.is_superuser:
        return render(request, "user/user_management.html")
    else:
        messages.add_message(request, messages.ERROR, "Users are not allowed to change other user's information.")
        return redirect('/')

