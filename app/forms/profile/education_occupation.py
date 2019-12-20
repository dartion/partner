from django import forms
from app.models import  ProfileBasicInfo,ProfileEducationOccupation

import datetime


class UpdateEducationOccupation(forms.ModelForm):
    data_exists = False
    def __init__(self, *args, **kwargs):
        profile_id = kwargs.pop('profile_id', None)
        super(UpdateEducationOccupation, self).__init__(*args, **kwargs)
        try:
            edu_occ_info_object = ProfileEducationOccupation.objects.get(profile_id=profile_id)
            self.fields['degree_or_diploma'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=edu_occ_info_object.degree_or_diploma)
            self.fields['pg_degree_or_diploma'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=edu_occ_info_object.pg_degree_or_diploma)
            self.fields['occupation'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=edu_occ_info_object.occupation)
            self.fields['place_of_occupation'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True, 'class': 'form-control form-control-lg'}),
                initial=edu_occ_info_object.place_of_occupation)
            self.fields['working_since'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=edu_occ_info_object.working_since)

            self.fields['average_monthly_income'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                initial=edu_occ_info_object.average_monthly_income)
            data_exists = True
        except Exception as ex:
            print(ex)
    degree_or_diploma = forms.CharField(widget=forms.TextInput(attrs={'required': False,'class':'form-control form-control-lg'}))
    pg_degree_or_diploma = forms.CharField(widget=forms.TextInput(attrs={'required': False,'class':'form-control form-control-lg'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'required': False,'class':'form-control form-control-lg'}))
    place_of_occupation = forms.CharField(
        widget=forms.TextInput(attrs={'required': False, 'class': 'form-control form-control-lg'}))
    working_since = forms.CharField(widget=forms.TextInput(attrs={'required': False,'class':'form-control form-control-lg'}))

    average_monthly_income = forms.CharField(widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}))

    class Meta:
        model = ProfileEducationOccupation
        fields = ('degree_or_diploma',
                  'pg_degree_or_diploma',
                  'occupation',
                  'place_of_occupation',
                  'working_since',
                  'average_monthly_income',

        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

    def save(self, profile_id, commit=True):
        degree_or_diploma = self.cleaned_data.get('degree_or_diploma')
        pg_degree_or_diploma = self.cleaned_data.get('pg_degree_or_diploma')
        occupation = self.cleaned_data.get('occupation')
        working_since = self.cleaned_data.get('working_since')
        place_of_occupation = self.cleaned_data.get('place_of_occupation')
        average_monthly_income = self.cleaned_data.get('average_monthly_income')

        try:
            print(profile_id)
            p = ProfileEducationOccupation.objects.get(profile_id=profile_id)
            p.degree_or_diploma = degree_or_diploma
            p.occupation = occupation
            p.working_since = working_since
            p.place_of_occupation = place_of_occupation
            p.average_monthly_income = average_monthly_income
            p.save()
            return p

        except Exception as ex:

            new_education_occupation_object = ProfileEducationOccupation.objects.create(
                degree_or_diploma = degree_or_diploma,
                pg_degree_or_diploma = pg_degree_or_diploma,
                occupation = occupation,

                working_since = working_since,
                place_of_occupation = place_of_occupation,
                average_monthly_income = average_monthly_income,
                profile=ProfileBasicInfo.objects.get(id=profile_id)

            )
            return new_education_occupation_object


class ViewEducationOccupation(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewEducationOccupation, self).__init__(*args, **kwargs)
        edu_occ_object = ProfileEducationOccupation.objects.get(profile_id=profile_object.id)

        self.fields['degree_or_diploma'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=edu_occ_object.degree_or_diploma)
        self.fields['pg_degree_or_diploma'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=edu_occ_object.pg_degree_or_diploma)
        self.fields['occupation'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=edu_occ_object.occupation)
        self.fields['place_of_occupation'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=edu_occ_object.place_of_occupation)
        self.fields['working_since'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=edu_occ_object.working_since)

        self.fields['average_monthly_income'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=edu_occ_object.average_monthly_income)




    class Meta:
        model = ProfileEducationOccupation
        fields = ('degree_or_diploma',
                  'pg_degree_or_diploma',
                  'occupation',
                  'place_of_occupation',
                  'working_since',
                  'average_monthly_income',

        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

