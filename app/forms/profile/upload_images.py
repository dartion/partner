from django import forms
from app.models import ProfileBasicInfo, ProfileImages, JatakaImages
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




class UploadJatakaImage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UploadJatakaImage, self).__init__(*args, **kwargs)


    class Meta:
        model = ProfileImages
        fields = ['jataka_image']

    def clean(self, *args, **kwargs):
        image = self.files.get('jataka_image')

        extension = str(image).rsplit('.')

        # if not extension[1] in ['jpeg','jpg','png']:
        #     raise forms.ValidationError("Image formats can be jpg, jpeg or png only.")
        return self.cleaned_data

    def save(self,profile_object):
        #title = self.cleaned_data.get('profile_image')
        jataka_image_1 = self.files.get('jataka_image')

        extension = str(jataka_image_1).rsplit('.')
        image_id = profile_object.id
        jataka_image = str(str(image_id)+"."+extension[1])
        img = self.files['jataka_image']
        img_extension = os.path.splitext(img.name)[1]

        user_folder = 'media/jataka/' + str(profile_object.id)
        if os.path.exists(user_folder):
            shutil.rmtree(user_folder)

        if not os.path.exists(user_folder):
            os.mkdir(user_folder)

        img_save_path = "{}/{}".format(user_folder, str(profile_object.id) +'.'+str(extension[1]))
        with open(img_save_path, 'wb+') as f:
            for chunk in img.chunks():
                f.write(chunk)

        try:
            object = JatakaImages.objects.create(profile=profile_object, jataka_image=jataka_image, url=img_save_path)
        except Exception as e:
            object = JatakaImages.objects.update(id=profile_object.id, jataka_image=jataka_image, url=img_save_path)
            return False
        return object
