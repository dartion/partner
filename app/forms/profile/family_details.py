from django import forms
from app.models import ProfileBasicInfo, ProfileFamilyDetails

import datetime


class UpdateFamilyDetails(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateFamilyDetails, self).__init__(*args, **kwargs)

    FAMILY_CLASS_CHOICES = [('Upper Middle Class', 'Upper Middle Class'),('Middle class','Middle class'), ('Lower Middle Class','Lower Middle Class')]
    FAMILY_TYPE_CHOICES = [('Joint Family', 'Joint Family'),('Nuclear Family','Nuclear Family')]
    FAMILY_VALUES_CHOICES = [('Orthodox','Orthodox'),('Traditional', 'Traditional'), ('Moderate','Moderate'), ('Liberal','Liberal')]
    MARRIED_CHOICES = [('Unmarried','Unmarried'), ('Divorcee','Divorcee')]

    family_class = forms.CharField(label='Family Class', widget=forms.Select(choices=FAMILY_CLASS_CHOICES))
    family_type = forms.CharField(label='Family Type', widget=forms.Select(choices=FAMILY_TYPE_CHOICES))
    family_values = forms.CharField(label='Family Values', widget=forms.Select(choices=FAMILY_VALUES_CHOICES))
    no_of_brothers = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    no_of_sisters = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    married = forms.CharField(label='Married Status', widget=forms.Select(choices=MARRIED_CHOICES))

    class Meta:
        model = ProfileFamilyDetails
        fields = ('family_class',
                  'family_type',
                  'family_values',
                  'no_of_brothers',
                  'no_of_sisters',
                  'married'
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

    def save(self, profile_id, commit=True):

        family_class = self.cleaned_data.get('family_class')
        family_type = self.cleaned_data.get('family_type')
        family_values = self.cleaned_data.get('family_values')
        no_of_brothers = self.cleaned_data.get('no_of_brothers')
        no_of_sisters = self.cleaned_data.get('no_of_sisters')
        married = self.cleaned_data.get('married')


        try:

            new_family_details_object = ProfileFamilyDetails.objects.create(
                family_class=family_class,
                family_type=family_type,
                family_values=family_values,
                no_of_brothers=no_of_brothers,
                no_of_sisters=no_of_sisters,
                married=married,
                profile=ProfileBasicInfo.objects.get(id=profile_id)
            )
            return new_family_details_object

        except Exception as ex:
            print("Profile Family Details cannot be updated  because {}".format(ex))
            return False


class ViewFamilyDetails(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewFamilyDetails, self).__init__(*args, **kwargs)
        family_deets_object = ProfileFamilyDetails.objects.get(profile_id=profile_object.id)


        FAMILY_CLASS_CHOICES = [('Upper Middle Class', 'Upper Middle Class'),('Middle class','Middle class'), ('Lower Middle Class','Lower Middle Class')]
        FAMILY_TYPE_CHOICES = [('Joint Family', 'Joint Family'),('Nuclear Family','Nuclear Family')]
        FAMILY_VALUES_CHOICES = [('Orthodox','Orthodox'),('Traditional', 'Traditional'), ('Moderate','Moderate'), ('Liberal','Liberal')]
        MARRIED_CHOICES = [('Unmarried','Unmarried'), ('Divorcee','Divorcee')]

        self.fields['family_class'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                              initial=family_deets_object.family_class)
        self.fields['family_type'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                              initial=family_deets_object.family_type)
        self.fields['family_values'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                              initial=family_deets_object.family_values)
        self.fields['no_of_brothers'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                              initial=family_deets_object.no_of_brothers)

        self.fields['no_of_sisters'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                     initial=family_deets_object.no_of_sisters)
        self.fields['married'] = forms.CharField(
            widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
            initial=family_deets_object.married)


    class Meta:
        model = ProfileFamilyDetails
        fields = ('family_class',
                  'family_type',
                  'family_values',
                  'no_of_brothers',
                  'no_of_sisters',
                  'married'
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

