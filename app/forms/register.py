#  partner - register.py
#
#  Description:
#  Author:           Darshan Nagavara (DN)
#  Created:          13 Nov. 2019
#  Source:           https://github.com/IntersectAustralia/partner
#  License:          Copyright (c) 2019 DN - All Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential
#

#  partner - register.py
#
#

from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    # Because we are using Django default user
    # it already has username property, therefore we just add email and password

    email = forms.EmailField(label="Email Address")
    email2 = forms.EmailField(label="Confirm Email Address")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Both the emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email is already registered")

        return super(UserRegisterForm, self).clean(*args, **kwargs)

