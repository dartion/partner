#  partner - reset_password.py
#
#  Description:
#  Author:           Darshan Nagavara (DN)
#  Created:          13 Nov. 2019
#  Source:           https://github.com/IntersectAustralia/partner
#  License:          Copyright (c) 2019 DN - All Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential
#

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from random import randint
from app.models import ResetPassword

class ResetPasswordForm(forms.Form):
    # Username = forms.CharField()
    Password = forms.CharField(label="Re-enter Password", widget=forms.PasswordInput)

    Password2 = forms.CharField(label="Re-enter Password", widget=forms.PasswordInput)



    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('Password')
        password2 = self.cleaned_data.get('Password2')
        if password != password2:
            raise forms.ValidationError("Password 1 and Password 2 must match")
        return self.cleaned_data


    def save(self, user):
        try:
            password = self.cleaned_data.get('Password')
            user.set_password(password)
            user.save()
            ResetPassword.objects.get(user_id=user).delete()

        except Exception as ex:
            return False
        return user




