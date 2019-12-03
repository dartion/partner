from django import forms
from app.models import ProfileBasicInfo, ProfileImages
from django.contrib.auth.models import User
import datetime

class UploadProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UploadProfileImage, self).__init__(*args, **kwargs)


    class Meta:
        model = ProfileImages
        fields = ['title', 'profile_image']

    # def clean(self, *args, **kwargs):
    #     # ToDo: Clean the input values as required here...
    #     image = self.cleaned_data['profile_image']
    #     return self.cleaned_data

    # def save(self):
    #     title = self.cleaned_data.get('title')
    #     # profile_image = self.profile_image.get('profile_image')
    #     profile_image1 = self.files.get('profile_image')
    #     print(title)
