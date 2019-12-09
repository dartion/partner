from django import forms
from app.models import ProfileBasicInfo
from django.contrib.auth.models import User
import datetime


class CreateProfile(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateProfile, self).__init__(*args, **kwargs)

    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}))
    gender = forms.CharField(label="Gender", widget=forms.Select(attrs={'class':'form-control form-control-lg'},choices=GENDER_CHOICES))
    dob = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(attrs={'required':True,'class':''}, years=range(1980,datetime.datetime.now().year)))
    phone_number = forms.CharField(label="Phone Number", widget=forms.NumberInput(
        attrs={'minlength':10, 'type': 'number', 'required': True, 'class':'form-control form-control-lg'}))
    phone_number_1 = forms.CharField(label="Additional Phone Number", widget=forms.NumberInput(
        attrs={'minlength': 10, 'type': 'number', 'class': 'form-control form-control-lg'}),required=False)
    phone_number_2 = forms.CharField(label="Additional Phone Number", widget=forms.NumberInput(
        attrs={'minlength': 10, 'type': 'number', 'class': 'form-control form-control-lg'}),required=False)
    profile_created_by = forms.CharField(label="Profile Created By",  widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}))

    class Meta:
        model = ProfileBasicInfo
        fields = ('first_name', 'last_name', 'gender', 'dob', 'profile_created_by')

    def clean(self, *args, **kwargs):
        #ToDo: Add validation rule for the following if necessary or remove the code
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        gender = self.cleaned_data.get('gender')
        phone_number = self.cleaned_data['phone_number']
        phone_number_1 = self.cleaned_data['phone_number_1']
        phone_number_2 = self.cleaned_data['phone_number_2']
        profile_created_by = self.cleaned_data['profile_created_by']
        # image = self.cleaned_data['image']
        if len(str(phone_number)) != 10:
            raise forms.ValidationError("Please enter the correct 10 digit phone number")

        dob = self.cleaned_data['rate'] = self.cleaned_data.get('dob')
        if dob.year >= datetime.datetime.now().year:
            raise forms.ValidationError("Date of birth cannot be the current year")


        try:
            profile_with_phone_number = ProfileBasicInfo.objects.filter(phone_number=phone_number).exists()
            if not profile_with_phone_number:
                pass
            else:
                raise forms.ValidationError("Profile with the following phone number is already registered. ")

        except Exception as ex:
            raise forms.ValidationError("Profile with the following phone number is already registered. ")

        return self.cleaned_data

    def save(self, id, commit=True):
        user = User.objects.get(id=id)
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        gender = self.cleaned_data.get('gender')
        dob = self.cleaned_data['rate'] = self.cleaned_data.get('dob')
        phone_number = self.cleaned_data['phone_number'] = self.cleaned_data.get('phone_number')
        phone_number_1 = self.cleaned_data['phone_number_1'] = self.cleaned_data.get('phone_number_1')
        phone_number_2 = self.cleaned_data['phone_number_2'] = self.cleaned_data.get('phone_number_2')
        if phone_number_1 == '':
            phone_number_1 = None
        if phone_number_2 == '':
            phone_number_2 = None
        # if phone_number_1 is not None:
        #     raise forms.ValidationError("Please enter the correct 10 digit phone number for Additional Phone Number 1")
        # if phone_number_2 is not None and len(phone_number_2) < 10:
        #     raise forms.ValidationError("Please enter the correct 10 digit phone number for Additional Phone Number 2")
        profile_created_by = self.cleaned_data.get('profile_created_by')

        try:

            new_profile_object = ProfileBasicInfo.objects.create(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                dob=dob,
                phone_number=phone_number,
                phone_number_1=phone_number_1,
                phone_number_2=phone_number_2,
                profile_created_by=profile_created_by,
                user=user,

            )
            return new_profile_object

        except Exception as ex:
            print("Profile creation failed because {}".format(ex))
            return False


class CreateProfileEdit(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(CreateProfileEdit, self).__init__(*args, **kwargs)
        GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
        try:
            profile_object = ProfileBasicInfo.objects.get(id=profile_object.id)
        except Exception as ex:
            profile_object.first_name=""
            profile_object.last_name=""
            profile_object.dob=""
            profile_object.gender=""
            profile_object.phone_number=""
            profile_object.phone_number_1=""
            profile_object.phone_number_2=""
            profile_object.profile_created_by=""

        self.fields['first_name'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}), initial=profile_object.first_name)
        self.fields['last_name'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),initial=profile_object.last_name)
        self.fields['dob'] = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(attrs={'required':True,}, years=range(1980,datetime.datetime.now().year)),initial=profile_object.dob)
        self.fields['gender'] = forms.CharField(label='Gender', widget=forms.Select(attrs={'class':'form-control form-control-lg'},choices=GENDER_CHOICES), initial=profile_object.gender)
        self.fields['phone_number'] = forms.CharField(label='Phone Number',widget=forms.TextInput(attrs={'class':'form-control form-control-lg','minlength':10, 'type': 'number', 'required': True}), initial=profile_object.phone_number)
        self.fields['phone_number_1'] = forms.CharField(label='Additional Phone Number',widget=forms.TextInput(attrs={'class':'form-control form-control-lg','minlength':10, 'type': 'number',}), initial=profile_object.phone_number_1,required=False)
        self.fields['phone_number_2'] = forms.CharField(label='Additional Phone Number',widget=forms.TextInput(attrs={'class':'form-control form-control-lg','minlength':10, 'type': 'number',}), initial=profile_object.phone_number_2,required=False)
        self.fields['profile_created_by'] = forms.CharField(
            widget=forms.TextInput(attrs={'required': True, 'class': 'form-control form-control-lg'}),
            initial=profile_object.profile_created_by)


    class Meta:
        model = ProfileBasicInfo
        fields = ('first_name', 'last_name', 'gender', 'dob', 'profile_created_by')

    def clean(self, *args, **kwargs):
        #ToDo: Add validation rule for the following if necessary or remove the code
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        gender = self.cleaned_data.get('gender')
        phone_number = self.cleaned_data['phone_number']
        phone_number_1 = self.cleaned_data['phone_number_1']
        phone_number_2 = self.cleaned_data['phone_number_2']
        if phone_number_1 == '':
            phone_number_1 = None
        if phone_number_2 == '':
            phone_number_2 = None

        # if phone_number_1 is not None and len(phone_number_1) < 10:
        #     raise forms.ValidationError("Please enter the correct 10 digit phone number for Additional Phone Number 1")
        # if phone_number_2 is not None and len(phone_number_2) < 10:
        #     raise forms.ValidationError("Please enter the correct 10 digit phone number for Additional Phone Number 2")
        profile_created_by = self.cleaned_data['profile_created_by']


        if len(str(phone_number)) != 10:
            raise forms.ValidationError("Please enter the correct 10 digit phone number")

        dob = self.cleaned_data['rate'] = self.cleaned_data.get('dob')
        if dob.year >= datetime.datetime.now().year:
            raise forms.ValidationError("Date of birth cannot be the current year")


        try:
            profile_with_phone_number = ProfileBasicInfo.objects.filter(phone_number=phone_number).exists()
            # if not profile_with_phone_number:
            #     pass
            # else:
            #     raise forms.ValidationError("Profile with the following phone number is already registered. ")

        except Exception as ex:
            raise forms.ValidationError("Profile with the following phone number is already registered. ")

        return self.cleaned_data

    def save(self, id, commit=True):
        updated_profile_object = ProfileBasicInfo.objects.get(id=id)
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        gender = self.cleaned_data.get('gender')
        dob = self.cleaned_data['rate'] = self.cleaned_data.get('dob')
        phone_number = self.cleaned_data['phone_number']
        phone_number_1 = self.cleaned_data['phone_number_1']
        phone_number_2 = self.cleaned_data['phone_number_2']
        profile_created_by = self.cleaned_data['profile_created_by']

        try:

            new_profile_object = ProfileBasicInfo.objects.get(id=id)
            new_profile_object.first_name=first_name
            new_profile_object.last_name=last_name
            new_profile_object.gender=gender
            new_profile_object.dob=dob
            new_profile_object.phone_number=phone_number
            new_profile_object.phone_number_1=phone_number_1
            new_profile_object.phone_number_2=phone_number_2
            new_profile_object.profile_created_by=profile_created_by

            new_profile_object.save()
            return updated_profile_object

        except Exception as ex:
            print("Profile update failed because {}".format(ex))
            return False

class CreateProfileView(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(CreateProfileView, self).__init__(*args, **kwargs)
        GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
        profile_object = ProfileBasicInfo.objects.get(id=profile_object.id)

        self.fields['first_name'] = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'required': True,'readOnly': True}), initial=profile_object.first_name)
        self.fields['last_name'] = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'required': True,'readOnly': True}),initial=profile_object.last_name)
        self.fields['dob'] = forms.CharField(label='Date of Birth', widget=forms.SelectDateWidget(attrs={'disabled':'disabled', 'readOnly': True}, years=range(1980,datetime.datetime.now().year)),initial=profile_object.dob)
        self.fields['gender'] = forms.CharField(label='Gender', widget=forms.Select(attrs={'class':'form-control form-control-lg', 'disabled':'disabled'},choices=GENDER_CHOICES), initial=profile_object.dob)
        self.fields['phone_number'] = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'minlength':10, 'type': 'number', 'readOnly': True,'required': True}), initial=profile_object.phone_number)
        self.fields['phone_number_1'] = forms.CharField(label='Additional Phone Number', widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'minlength':10, 'type': 'number', 'readOnly': True,'required': True}), initial=profile_object.phone_number_1)
        self.fields['phone_number_2'] = forms.CharField(label='Additional Phone Number', widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'minlength':10, 'type': 'number', 'readOnly': True,'required': True}), initial=profile_object.phone_number_2)

        self.fields['profile_created_by'] = forms.CharField(label='Last Name', widget=forms.TextInput(
            attrs={'class': 'form-control form-control-lg', 'required': True, 'readOnly': True}),
                                                   initial=profile_object.profile_created_by)

    class Meta:
        model = ProfileBasicInfo
        fields = ('first_name', 'last_name', 'gender', 'dob','profile_created_by')

    def clean(self, *args, **kwargs):
        #ToDo: Add validation rule for the following if necessary or remove the code
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        gender = self.cleaned_data.get('gender')
        phone_number = self.cleaned_data['phone_number']
        phone_number_1 = self.cleaned_data['phone_number_1']
        phone_number_2 = self.cleaned_data['phone_number_2']
        profile_created_by = self.cleaned_data['profile_created_by']


        if len(str(phone_number)) != 10:
            raise forms.ValidationError("Please enter the correct 10 digit phone number")

        dob = self.cleaned_data['rate'] = self.cleaned_data.get('dob')
        if dob.year >= datetime.datetime.now().year:
            raise forms.ValidationError("Date of birth cannot be the current year")


        try:
            profile_with_phone_number = ProfileBasicInfo.objects.filter(phone_number=phone_number).exists()

        except Exception as ex:
            raise forms.ValidationError("Profile with the following phone number is already registered. ")

        return self.cleaned_data

