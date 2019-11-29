from django import forms
from app.models import  ProfileBasicInfo,ProfileEducationOccupation

import datetime


class UpdateEducationOccupation(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateEducationOccupation, self).__init__(*args, **kwargs)

    degree_or_diploma = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    pg_degree_or_diploma = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    working_since = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    place_of_occupation = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    average_monthly_income = forms.CharField(widget=forms.TextInput(attrs={'required': True}))

    class Meta:
        model = ProfileEducationOccupation
        fields = ('degree_or_diploma',
                  'pg_degree_or_diploma',
                  'occupation',
                  'working_since',
                  'place_of_occupation',
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

        except Exception as ex:
            print("Profile Education/Occupation Info cannot be updated  because {}".format(ex))
            return False


class ViewEducationOccupation(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewEducationOccupation, self).__init__(*args, **kwargs)
        edu_occ_object = ProfileEducationOccupation.objects.get(profile_id=profile_object.id)

        self.fields['degree_or_diploma'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                initial=edu_occ_object.degree_or_diploma)
        self.fields['pg_degree_or_diploma'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                initial=edu_occ_object.pg_degree_or_diploma)
        self.fields['occupation'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                initial=edu_occ_object.occupation)
        self.fields['working_since'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                initial=edu_occ_object.working_since)
        self.fields['place_of_occupation'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                initial=edu_occ_object.place_of_occupation)
        self.fields['average_monthly_income'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                        initial=edu_occ_object.average_monthly_income)




    class Meta:
        model = ProfileEducationOccupation
        fields = ('degree_or_diploma',
                  'pg_degree_or_diploma',
                  'occupation',
                  'working_since',
                  'place_of_occupation',
                  'average_monthly_income',

        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

