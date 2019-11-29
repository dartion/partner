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

from django import forms
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    # Username = forms.CharField()
    # Password = forms.CharField(widget=forms.PasswordInput)
    Username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
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
    Password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg',
                                                                                   'placeholder': ' ',
                                                                                   'id': 'password',
                                                                                   'name': 'j_password',
                                                                                   'type': 'password',
                                                                                   'value': '',
                                                                                   'autocorrect': 'off',
                                                                                   'autocapitalize': 'none',
                                                                                   'autocomplete': 'new-password'
                                                                                   },
                                                                            render_value=True
                                                                            )
                               )

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('Username')
        password = self.cleaned_data.get('Password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Username or password is incorrect.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is NOT active")

        return super(UserLoginForm, self).clean(*args, **kwargs)





