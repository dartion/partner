from django import forms
from app.models import ProfileBasicInfo, ProfileImages, HoroscopeImages
from django.contrib.auth.models import User
import datetime, os, shutil


class UploadProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UploadProfileImage, self).__init__(*args, **kwargs)


    class Meta:
        model = ProfileImages
        fields = [ 'profile_image']

    def clean(self, *args, **kwargs):
        image = self.files.get('profile_image')

        extension = str(image).rsplit('.')

        # if not extension[1] in ['jpeg','jpg','png']:
        #     raise forms.ValidationError("Image formats can be jpg, jpeg or png only.")
        return self.cleaned_data

    def save(self,profile_object):
        #title = self.cleaned_data.get('profile_image')
        profile_image_1 = self.files.get('profile_image')

        extension = str(profile_image_1).rsplit('.')
        image_id = profile_object.id
        profile_image = str(str(image_id)+"."+extension[1])
        img = self.files['profile_image']
        img_extension = os.path.splitext(img.name)[1]

        user_folder = 'media/profile/' + str(profile_object.id)
        if os.path.exists(user_folder):
            shutil.rmtree(user_folder)

        if not os.path.exists(user_folder):
            os.mkdir(user_folder)

        img_save_path = "{}/{}".format(user_folder, str(profile_object.id) +'.'+str(extension[1]))
        with open(img_save_path, 'wb+') as f:
            for chunk in img.chunks():
                f.write(chunk)

        try:
            object = ProfileImages.objects.create(profile=profile_object, profile_image=profile_image, url=img_save_path)
        except Exception as e:
            object = ProfileImages.objects.update(id=profile_object.id, profile_image=profile_image, url=img_save_path)
            return False
        return object




class UploadHoroscopeImage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UploadHoroscopeImage, self).__init__(*args, **kwargs)


    class Meta:
        model = ProfileImages
        fields = ['horoscope_image']

    def clean(self, *args, **kwargs):
        image = self.files.get('horoscope_image')

        extension = str(image).rsplit('.')

        # if not extension[1] in ['jpeg','jpg','png']:
        #     raise forms.ValidationError("Image formats can be jpg, jpeg or png only.")
        return self.cleaned_data

    def save(self,profile_object):
        #title = self.cleaned_data.get('profile_image')
        horoscope_image_1 = self.files.get('horoscope_image')

        extension = str(horoscope_image_1).rsplit('.')
        image_id = profile_object.id
        horoscope_image = str(str(image_id)+"."+extension[1])
        img = self.files['horoscope_image']
        img_extension = os.path.splitext(img.name)[1]

        user_folder = 'media/horoscope/' + str(profile_object.id)
        if os.path.exists(user_folder):
            shutil.rmtree(user_folder)

        if not os.path.exists(user_folder):
            os.mkdir(user_folder)

        img_save_path = "{}/{}".format(user_folder, str(profile_object.id) +'.'+str(extension[1]))
        with open(img_save_path, 'wb+') as f:
            for chunk in img.chunks():
                f.write(chunk)

        try:
            object = HoroscopeImages.objects.create(profile=profile_object, horoscope_image=horoscope_image, url=img_save_path)
        except Exception as e:
            object = HoroscopeImages.objects.update(id=profile_object.id, horoscope_image=horoscope_image, url=img_save_path)
            return False
        return object
