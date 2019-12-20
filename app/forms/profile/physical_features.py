#  partner -   physical_features.py
#  Description:
#  Author:           darshan
#  Created:          21 Dec. 2019
#  Source:           https://github.com/dartion/partner
#  License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential

from django import forms
from app.models import  ProfileBasicInfo, ProfilePhysicalFeatures

import datetime


class UpdatePhysicalFeatures(forms.ModelForm):
    data_exists = False


    def __init__(self, *args, **kwargs):
        profile_id = kwargs.pop('profile_id', None)
        super(UpdatePhysicalFeatures, self).__init__(*args, **kwargs)

        try:
            BODY_TYPE_CHOICES = [('Athletic', 'Athletic'), ('Heavy', 'Heavy'), ('Normal', 'Normal'),
                                 ('Average', 'Average')]
            COMPLEXION_CHOICES = [('Very Fair', 'Very Fair'), ('Fair', 'Fair'), ('Wheatish', 'Wheatish'),
                                  ('Brown', 'Brown'), ('Dark', 'Dark')]
            PHYSICAL_STATUS_CHOICES = [('Normal', 'Normal'), ('Physically Handicapped', 'Physically Handicapped')]

            physical_info_object = ProfilePhysicalFeatures.objects.get(profile_id=profile_id)
            self.fields['height'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}),
                                                    initial=physical_info_object.height)
            self.fields['body_type'] = forms.CharField(
                widget=forms.Select(choices=BODY_TYPE_CHOICES, attrs={'class':'form-control form-control-lg'}),
                initial=physical_info_object.body_type)
            self.fields['complexion'] = forms.CharField(
                widget=forms.Select(choices=COMPLEXION_CHOICES,attrs={'class':'form-control form-control-lg'} ),
                initial=physical_info_object.complexion)
            self.fields['physical_status'] = forms.CharField(
                widget=forms.Select(choices=PHYSICAL_STATUS_CHOICES,attrs={'class':'form-control form-control-lg'} ),
                initial=physical_info_object.physical_status)
            self.fields['blood_group'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}),
                initial=physical_info_object.blood_group)
            data_exists = True
        except Exception as ex:
            print(ex)

    BODY_TYPE_CHOICES = [('Athletic', 'Athletic'), ('Heavy', 'Heavy'), ('Normal', 'Normal'),
                         ('Average', 'Average')]
    COMPLEXION_CHOICES = [('Very Fair', 'Very Fair'), ('Fair', 'Fair'), ('Wheatish', 'Wheatish'),
                          ('Brown', 'Brown'),
                          ('Dark', 'Dark')]
    PHYSICAL_STATUS_CHOICES = [('Normal', 'Normal'), ('Physically Handicapped', 'Physically Handicapped')]

    height = forms.CharField(
        widget=forms.TextInput(attrs={'required': True, 'class': 'form-control form-control-lg'}))
    body_type = forms.CharField(label='Body Type', widget=forms.Select(choices=BODY_TYPE_CHOICES, attrs={
        'class': 'form-control form-control-lg'}))
    complexion = forms.CharField(label='Complexion', widget=forms.Select(choices=COMPLEXION_CHOICES, attrs={
        'class': 'form-control form-control-lg'}))
    physical_status = forms.CharField(label='Physical Status',
                                      widget=forms.Select(choices=PHYSICAL_STATUS_CHOICES,
                                                          attrs={'class': 'form-control form-control-lg'}))
    blood_group = forms.CharField(
        widget=forms.TextInput(attrs={'required': True, 'class': 'form-control form-control-lg'}))


    class Meta:
        model = ProfilePhysicalFeatures
        fields = ('height',
                  'body_type',
                  'complexion',
                  'physical_status',
                  'blood_group'
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

    def save(self, profile_id, commit=True):
        height = self.cleaned_data.get('height')
        body_type = self.cleaned_data.get('body_type')
        complexion = self.cleaned_data.get('complexion')
        physical_status = self.cleaned_data.get('physical_status')
        blood_group = self.cleaned_data.get('blood_group')


        try:
            print (profile_id)
            p = ProfilePhysicalFeatures.objects.get(profile_id=profile_id)
            p.height = height
            p.body_type=body_type
            p.complexion=complexion
            p.physical_status= physical_status
            p.blood_group = blood_group
            p.save()
            return p

        except Exception as ex:
            new_personal_info_object = ProfilePhysicalFeatures.objects.create(
                    height = height,
                    body_type = body_type,
                    complexion = complexion,
                    physical_status = physical_status,
                    blood_group = blood_group,
                    profile=ProfileBasicInfo.objects.get(id=profile_id)
                )
            return new_personal_info_object


        print("Profile physical features information Info cannot be updated  because {}".format(ex))
        return False

class ViewPhysicalFeatures(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewPhysicalFeatures, self).__init__(*args, **kwargs)
        try:
            physical_info_object = ProfilePhysicalFeatures.objects.get(profile_id=profile_object.id)
        except Exception as ex:
            print(ex)
        BODY_TYPE_CHOICES = [('Athletic','Athletic'),('Heavy', 'Heavy'), ('Normal', 'Normal'), ('Average', 'Average')]
        COMPLEXION_CHOICES = [('Very Fair','Very Fair'),('Fair','Fair'),('Wheatish','Wheatish'), ('Brown', 'Brown'), ('Dark', 'Dark')]
        PHYSICAL_STATUS_CHOICES = [('Normal','Normal'),('Physically Handicapped', 'Physically Handicapped')]

        self.fields['height'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True,'class': 'form-control form-control-lg'}),
                                                    initial=physical_info_object.height)
        self.fields['body_type'] = forms.CharField(widget=forms.Select(choices=BODY_TYPE_CHOICES, attrs={'disabled':'disabled','class': 'form-control form-control-lg'}),
                                                    initial=physical_info_object.body_type)
        self.fields['complexion'] = forms.CharField(widget=forms.Select(choices=COMPLEXION_CHOICES, attrs={'disabled':'disabled','class': 'form-control form-control-lg'}),
                                                    initial=physical_info_object.complexion)
        self.fields['physical_status'] = forms.CharField(widget=forms.Select(choices=PHYSICAL_STATUS_CHOICES,attrs={'disabled':'disabled','class': 'form-control form-control-lg'}),
                                                    initial=physical_info_object.physical_status)
        self.fields['blood_group'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True,'class': 'form-control form-control-lg'}),
                                                    initial=physical_info_object.blood_group)


    class Meta:
        model = ProfilePhysicalFeatures
        fields = ('height',
                  'body_type',
                  'complexion',
                  'physical_status',
                  'blood_group'
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

