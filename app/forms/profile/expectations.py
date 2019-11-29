from django import forms
from app.models import  ProfileBasicInfo, ProfileExpectation

import datetime


class UpdateExpectations(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_id = kwargs.pop('profile_id', None)
        super(UpdateExpectations, self).__init__(*args, **kwargs)
        try:
            expectations_object = UpdateExpectations.objects.get(profile_id=profile_id)
            self.fields['expectations'] = forms.CharField(
            widget=forms.TextInput(attrs={'required': True}),
            initial=expectations_object.expectations)
        except Exception as ex:
            expectations = forms.CharField(widget=forms.TextInput(attrs={'required': True}))

    class Meta:
        model = ProfileExpectation
        fields = ('expectations',
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

    def save(self, profile_id, commit=True):
        expectations = self.cleaned_data.get('expectations')

        try:
            p = ProfileExpectation.objects.get(profile_id=profile_id)
            p.expectations = expectations
            p.save()
            return p
        except Exception as Ex:
            new_expectations_object = ProfileExpectation.objects.create(
                expectations = expectations,
                profile=ProfileBasicInfo.objects.get(id=profile_id)
            )
            return new_expectations_object

class ViewExpectations(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewExpectations, self).__init__(*args, **kwargs)
        expectations_object = ProfileExpectation.objects.get(profile_id=profile_object.id)

        self.fields['expectations'] = forms.CharField(
            widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
            initial=expectations_object.expectations)


    class Meta:
        model = ProfileExpectation
        fields = ('expectations',
        )


