from django import forms
from app.models import  ProfilePersonalInfo,ProfileBasicInfo

import datetime


class UpdateProfilePersonalInfo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateProfilePersonalInfo, self).__init__(*args, **kwargs)

    fathers_name = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    mothers_name = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    guardians_name = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    resident_of_country = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    resident_of_state = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    resident_of_city_or_village = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    mother_toungue = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    community = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    caste = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    sub_caste = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    native_place = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    residential_address = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    additional_info = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'required': True}))


    class Meta:
        model = ProfilePersonalInfo
        fields = ('fathers_name',
                  'mothers_name',
                  'guardians_name',
                  'resident_of_country',
                  'resident_of_state',
                  'resident_of_city_or_village',
                  'mother_toungue',
                  'community',
                  'caste',
                  'sub_caste',
                  'native_place',
                  'residential_address',
                  'contact_number',
                  'additional_info',
                  'email'
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

    def save(self, profile_id, commit=True):
        fathers_name = self.cleaned_data.get('fathers_name')
        mothers_name = self.cleaned_data.get('mothers_name')
        guardians_name = self.cleaned_data.get('guardians_name')
        resident_of_country = self.cleaned_data.get('resident_of_country')
        resident_of_state = self.cleaned_data.get('resident_of_state')
        resident_of_city_or_village = self.cleaned_data.get('resident_of_city_or_village')
        mother_toungue = self.cleaned_data.get('mother_toungue')
        community = self.cleaned_data.get('community')
        caste = self.cleaned_data.get('caste')
        sub_caste = self.cleaned_data.get('sub_caste')
        native_place = self.cleaned_data.get('native_place')
        residential_address = self.cleaned_data.get('residential_address')
        contact_number = self.cleaned_data.get('contact_number')
        additional_info = self.cleaned_data.get('additional_info')
        email = self.cleaned_data.get('email')



        try:
            new_personal_info_object = ProfilePersonalInfo.objects.create(
                fathers_name = fathers_name,
                mothers_name = mothers_name,
                guardians_name = guardians_name,
                resident_of_country = resident_of_country,
                resident_of_state = self.cleaned_data.get('resident_of_state'),
                resident_of_city_or_village = resident_of_city_or_village,
                mother_toungue = self.cleaned_data.get('mother_toungue'),
                community = community,
                caste = caste,
                sub_caste = sub_caste,
                native_place = native_place,
                residential_address = residential_address,
                contact_number = contact_number,
                additional_info = additional_info,
                email = email,
                profile=ProfileBasicInfo.objects.get(id=profile_id)
            )
            return new_personal_info_object

        except Exception as ex:
            print("Profile personal Info cannot be updated  because {}".format(ex))
            return False

class ViewProfilePersonalInfo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewProfilePersonalInfo, self).__init__(*args, **kwargs)

        personal_info_object = ProfilePersonalInfo.objects.get(profile_id=profile_object.id)

        self.fields['fathers_name'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                initial=personal_info_object.fathers_name)

        self.fields['mothers_name'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                  initial=personal_info_object.fathers_name)

        self.fields['guardians_name'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                      initial=personal_info_object.fathers_name)
        self.fields['resident_of_country'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                      initial=personal_info_object.fathers_name)
        self.fields['resident_of_state'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                      initial=personal_info_object.fathers_name)
        self.fields['resident_of_city_or_village'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                      initial=personal_info_object.fathers_name)
        self.fields['mother_toungue'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                                     initial=personal_info_object.fathers_name)
        self.fields['community'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                                     initial=personal_info_object.fathers_name)
        self.fields['caste'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                                     initial=personal_info_object.fathers_name)
        self.fields['sub_caste'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                                     initial=personal_info_object.fathers_name)
        self.fields['native_place'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                                     initial=personal_info_object.fathers_name)

        self.fields['residential_address'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                      initial=personal_info_object.fathers_name)

        self.fields['contact_number'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                  initial=personal_info_object.fathers_name)

        self.fields['additional_info'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                  initial=personal_info_object.fathers_name)

        self.fields['email'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'readOnly': True}),
                                                  initial=personal_info_object.fathers_name)


    class Meta:
        model = ProfilePersonalInfo
        fields = ('fathers_name',
                  'mothers_name',
                  'guardians_name',
                  'resident_of_country',
                  'resident_of_state',
                  'resident_of_city_or_village',
                  'mother_toungue',
                  'community',
                  'caste',
                  'sub_caste',
                  'native_place',
                  'residential_address',
                  'contact_number',
                  'additional_info',
                  'email'
        )


