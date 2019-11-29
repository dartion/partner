from django import forms
from app.models import  ProfileBasicInfo, ProfileHabbits

import datetime


class UpdateHabbits(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateHabbits, self).__init__(*args, **kwargs)

    FOOD_CHOICES = [('Vegetarian', 'Vegetarian'),('Non-Vegetarian','Non-Vegetarian'), ('Eggetarian','Eggetarian')]
    SMOKING_CHOICES = [('Yes', 'Yes'),('No','No'), ('Occasionally','Occasionally')]
    ACHOHOLIC_DRINKS_CHOICES = [('Yes', 'Yes'),('No','No'), ('Occasionally','Occasionally')]

    food = forms.CharField(label='Food ', widget=forms.Select(choices=FOOD_CHOICES))
    smoking = forms.CharField(label='Smoking', widget=forms.Select(choices=SMOKING_CHOICES))
    alcholic_drinks = forms.CharField(label='Alcoholic Drinks', widget=forms.Select(choices=ACHOHOLIC_DRINKS_CHOICES))


    class Meta:
        model = ProfileHabbits
        fields = ('food',
                  'smoking',
                  'alcholic_drinks',
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

    def save(self, profile_id, commit=True):

        food = self.cleaned_data.get('food')
        smoking = self.cleaned_data.get('smoking')
        alcholic_drinks = self.cleaned_data.get('alcholic_drinks')

        try:

            new_habbits_object = ProfileHabbits.objects.create(
                food=food ,
                smoking=smoking ,
                alcholic_drinks=alcholic_drinks,
                profile=ProfileBasicInfo.objects.get(id=profile_id)
            )
            return new_habbits_object

        except Exception as ex:
            print("Profile habbits cannot be updated  because {}".format(ex))
            return False

class ViewHabbits(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewHabbits, self).__init__(*args, **kwargs)
        habbits_object = ProfileHabbits.objects.get(profile_id=profile_object.id)


        FOOD_CHOICES = [('Vegetarian', 'Vegetarian'),('Non-Vegetarian','Non-Vegetarian'), ('Eggetarian','Eggetarian')]
        SMOKING_CHOICES = [('Yes', 'Yes'),('No','No'), ('Occasionally','Occasionally')]
        ACHOHOLIC_DRINKS_CHOICES = [('Yes', 'Yes'),('No','No'), ('Occasionally','Occasionally')]

        self.fields['food'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                initial=habbits_object.food)
        self.fields['smoking'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                initial=habbits_object.smoking)
        self.fields['alcholic_drinks'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                initial=habbits_object.alcholic_drinks)


    class Meta:
        model = ProfileHabbits
        fields = ('food',
                  'smoking',
                  'alcholic_drinks',
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

