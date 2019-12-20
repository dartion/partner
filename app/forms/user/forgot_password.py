#  partner -   forgot_password.py
#  Description:
#  Author:           darshan
#  Created:          21 Dec. 2019
#  Source:           https://github.com/dartion/partner
#  License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential

#  partner - forgot_password.py
#
#

from django import forms
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from random import randint
from app.models import ResetPassword
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader



class ForgotPasswordForm(forms.Form):
    # Username = forms.CharField()
    # Password = forms.CharField(widget=forms.PasswordInput)
    Username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-field form-element',
                                                                               'placeholder': ' ',
                                                                               'id': 'username',
                                                                               'name': 'j_username',
                                                                               'type': 'text',
                                                                               'autocorrect': 'off',
                                                                               'autocapitalize': 'none',
                                                                               'value': ''
                                                                               }
                                                                        )
                               )

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('Username')
        # Look in the database for the user name
        # If the username exists

        try:
            user = User.objects.get(username=username)
        except Exception as ex:
            raise forms.ValidationError("The username does not exist in the system. Please contact +91 99222111122 for more informtion")

        return self.cleaned_data


    def save(self):
        username = self.cleaned_data.get('Username')
        user = User.objects.get(username=username)
        unique_number = randint(10000, 99999)
        print(user.id)
        try:
            check_if_user_exists = ResetPassword.objects.get(user=user)
            check_if_user_exists.reset_password_number = unique_number
            check_if_user_exists.save()
        except Exception as ex:
            reset_password_object = ResetPassword.objects.create(user=user,
                                                                           reset_password_number=unique_number)

        subject = 'Reset Password'

        message = ''
        html_message = render_to_string('forgot_password/reset_password_template.html',
                                        {'username': user.username,
                                         'url': "{}/reset_password/{}/{}".format(settings.ALLOWED_HOSTS[0], user.id, unique_number)})
        email_from = settings.EMAIL_SENDER
        recipient_list = [user.email]
        send_mail(subject, message, from_email=email_from, recipient_list=recipient_list, html_message=html_message)

        # Email the link.
        return True




