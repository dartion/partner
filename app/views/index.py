#  partner - login.py
#
#  Description:
#  Author:           Darshan Nagavara (DN)
#  Created:          13 Nov. 2019
#  Source:           https://github.com/IntersectAustralia/partner
#  License:          Copyright (c) 2019 DN - All Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential
#

#  partner - login.py
#
#

#  partner - login.py
#
#

from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms.login import UserLoginForm
from app.forms.register import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username_from_form = form.cleaned_data.get('username')
        password_from_form = form.cleaned_data.get('password')
        user = authenticate(username=username_from_form, password=password_from_form)

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
        password = form.cleaned_data.get('password')

        user.set_password(password)
        user.is_active = True

        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, "login/register.html", context)

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def index(request):
    return HttpResponse("This is the HOME PAGE")