#  partner -   personal_info.py
#  Description:
#  Author:           darshan
#  Created:          21 Dec. 2019
#  Source:           https://github.com/dartion/partner
#  License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential

from django import forms
from app.models import  ProfilePersonalInfo,ProfileBasicInfo

import datetime


class UpdateProfilePersonalInfo(forms.ModelForm):
    data_exists = False
    def __init__(self, *args, **kwargs):
        profile_id = kwargs.pop('profile_id', None)
        super(UpdateProfilePersonalInfo, self).__init__(*args, **kwargs)
        try:
            personal_info_object = ProfilePersonalInfo.objects.get(profile_id=profile_id)
            self.fields['fathers_name'] = forms.CharField(label="Father's Name",
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg '}),
                initial=personal_info_object.fathers_name)

            self.fields['mothers_name'] = forms.CharField(label="Mother's Occupation",
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.mothers_name)

            self.fields['guardians_name'] = forms.CharField(label="Gaurdian's Occupation",
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.guardians_name)

            self.fields['fathers_occupation'] = forms.CharField(label="Father's Occupation",
                widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                initial=personal_info_object.fathers_occupation, required=False)

            self.fields['mothers_occupation'] = forms.CharField(label="Mother's Occupation",
                widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                initial=personal_info_object.mothers_occupation, required=False)

            self.fields['guardians_occupation'] = forms.CharField(label="Gaurdian's Occupation",
                widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                initial=personal_info_object.guardians_occupation, required=False)

            self.fields['resident_of_country'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.resident_of_country)
            self.fields['resident_of_state'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.resident_of_state)
            self.fields['resident_of_city_or_village'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.resident_of_city_or_village)
            self.fields['mother_tongue'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.mother_tongue)
            self.fields['community'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.community)
            self.fields['caste'] = forms.CharField(label="Caste / Sub-caste",widget=forms.TextInput(attrs={'required': True,
                                                                                 'class':'form-control form-control-lg'}),
                                                   initial=personal_info_object.caste)

            self.fields['native_place'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.native_place)

            self.fields['residential_address'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.residential_address)

            self.fields['contact_number'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.contact_number)

            self.fields['additional_info'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=personal_info_object.additional_info)

            self.fields['email'] = forms.CharField(widget=forms.TextInput(attrs={'required':False, 'class':'form-control form-control-lg'}),
                                                   initial=personal_info_object.email, required=False)
            data_exists = True
        except Exception as e:
            print (e)

    if data_exists == False:
        fathers_name = forms.CharField(label="Father's Name",widget=forms.TextInput(attrs={'required': False, 'class':'form-control form-control-lg'}))
        mothers_name = forms.CharField(label="Mother's Name",widget=forms.TextInput(attrs={'required': False, 'class':'form-control form-control-lg'}))
        guardians_name = forms.CharField(label="Gaurdian's Name",widget=forms.TextInput(attrs={'required': False, 'class':'form-control form-control-lg'}))

        fathers_occupation = forms.CharField(label="Father's Occupation",
            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), required=False)
        mothers_occupation = forms.CharField(label="Mother's Occupation",
            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), required=False)
        guardians_occupation = forms.CharField(label="Gaurdian's Occupation",
            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), required=False)

        resident_of_country = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}))
        resident_of_state = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}))
        resident_of_city_or_village = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}))
        mother_tongue = forms.CharField(widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}))
        community = forms.CharField(widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}))

        caste = forms.CharField(label="Caste / Sub-caste",
            widget=forms.TextInput(attrs={'required': True, 'class': 'form-control form-control-lg'}))

        native_place = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}))
        residential_address = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}))
        contact_number = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}))
        additional_info = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}))
        email = forms.CharField(widget=forms.TextInput(attrs={'required':False, 'class': 'form-control form-control-lg'}), required=False)

    class Meta:
        model = ProfilePersonalInfo
        fields = ('fathers_name',
                  'mothers_name',
                  'guardians_name',
                  'fathers_occupation',
                  'mothers_occupation',
                  'guardians_occupation',
                  'resident_of_country',
                  'resident_of_state',
                  'resident_of_city_or_village',
                  'mother_tongue',
                  'community',
                  'caste',
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
        fathers_occupation = self.cleaned_data.get('fathers_occupation')
        mothers_occupation = self.cleaned_data.get('mothers_occupation')
        guardians_occupation = self.cleaned_data.get('guardians_occupation')
        resident_of_country = self.cleaned_data.get('resident_of_country')
        resident_of_state = self.cleaned_data.get('resident_of_state')
        resident_of_city_or_village = self.cleaned_data.get('resident_of_city_or_village')
        mother_tongue = self.cleaned_data.get('mother_tongue')
        community = self.cleaned_data.get('community')
        caste = self.cleaned_data.get('caste')
        native_place = self.cleaned_data.get('native_place')
        residential_address = self.cleaned_data.get('residential_address')
        contact_number = self.cleaned_data.get('contact_number')
        additional_info = self.cleaned_data.get('additional_info')
        email = self.cleaned_data.get('email')


        try:
            if ProfilePersonalInfo.objects.get(profile_id=profile_id):
                p = ProfilePersonalInfo.objects.get(profile_id=profile_id)
                p.fathers_name=fathers_name
                p.mothers_name=mothers_name
                p.guardians_name=guardians_name
                p.fathers_occupation = fathers_occupation
                p.mothers_occupation = mothers_occupation
                p.guardians_occupation=guardians_occupation
                p.resident_of_country=resident_of_country
                p.resident_of_state=self.cleaned_data.get('resident_of_state')
                p.resident_of_city_or_village=resident_of_city_or_village
                p.mother_tongue=self.cleaned_data.get('mother_tongue')
                p.community=community
                p.caste=caste
                p.native_place=native_place
                p.residential_address=residential_address
                p.contact_number=contact_number
                p.additional_info=additional_info
                p.email=email
                p.save()
                return p


        except Exception as ex:
            new_personal_info_object = ProfilePersonalInfo.objects.create(
                fathers_name=fathers_name,
                mothers_name=mothers_name,
                guardians_name=guardians_name,
                fathers_occupation = fathers_occupation,
                mothers_occupation = mothers_occupation,
                guardians_occupation = guardians_occupation,
                resident_of_country=resident_of_country,
                resident_of_state=self.cleaned_data.get('resident_of_state'),
                resident_of_city_or_village=resident_of_city_or_village,
                mother_tongue=self.cleaned_data.get('mother_tongue'),
                community=community,
                caste=caste,
                native_place=native_place,
                residential_address=residential_address,
                contact_number=contact_number,
                additional_info=additional_info,
                email=email,
                profile=ProfileBasicInfo.objects.get(id=profile_id)
            )
            return new_personal_info_object

        print("Profile physical features information Info cannot be updated.")
        return False

class ViewProfilePersonalInfo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewProfilePersonalInfo, self).__init__(*args, **kwargs)

        personal_info_object = ProfilePersonalInfo.objects.get(profile_id=profile_object.id)

        self.fields['fathers_name'] = forms.CharField(label="Father's Name",
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.fathers_name)

        self.fields['mothers_name'] = forms.CharField(label="Mother's Name",
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.mothers_name)

        self.fields['guardians_name'] = forms.CharField(label="Guardians's Name",
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.guardians_name)

        self.fields['fathers_occupation'] = forms.CharField(label="Father's Occupation",
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.fathers_occupation)

        self.fields['mothers_occupation'] = forms.CharField(label="Mother's Occupation",
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.mothers_occupation)
        self.fields['guardians_occupation'] = forms.CharField(label="Gaurdian's Occupation",
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.guardians_occupation)

        self.fields['resident_of_country'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.resident_of_country)
        self.fields['resident_of_state'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.resident_of_state)
        self.fields['resident_of_city_or_village'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.resident_of_city_or_village)
        self.fields['mother_tongue'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.mother_tongue)
        self.fields['community'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.community)
        self.fields['caste'] = forms.CharField(label="Caste/Sub-caste", widget=forms.TextInput(attrs={'readOnly': True,
                                                                             'class': 'form-control form-control-lg'}),
                                               initial=personal_info_object.caste)
        self.fields['native_place'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.native_place)

        self.fields['residential_address'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.residential_address)

        self.fields['contact_number'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.contact_number)

        self.fields['additional_info'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.additional_info)

        self.fields['email'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=personal_info_object.email)


    class Meta:
        model = ProfilePersonalInfo
        fields = ('fathers_name',
                  'mothers_name',
                  'guardians_name',
                  'fathers_occupation',
                  'mothers_occupation',
                  'guardians_occupation',
                  'resident_of_country',
                  'resident_of_state',
                  'resident_of_city_or_village',
                  'mother_tongue',
                  'community',
                  'caste',
                  'native_place',
                  'residential_address',
                  'contact_number',
                  'additional_info',
                  'email'
        )


