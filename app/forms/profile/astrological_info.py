from django import forms
from app.models import ProfileBasicInfo, ProfileAstrologicalInfo

import datetime


class UpdateAstrologicalInfo(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateAstrologicalInfo, self).__init__(*args, **kwargs)

    gothra = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    pravara = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    nakshatra = forms.CharField(widget=forms.TextInput(attrs={'required': False}))
    rashi = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    horoscope_matching = forms.CharField(widget=forms.TextInput(attrs={'required': True}))


    class Meta:
        model = ProfileAstrologicalInfo
        fields = ('gothra',
                  'pravara',
                  'nakshatra',
                  'rashi',
                  'horoscope_matching'
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

    def save(self, profile_id, commit=True):

        gothra = self.cleaned_data.get('gothra')
        pravara = self.cleaned_data.get('pravara')
        nakshatra = self.cleaned_data.get('nakshatra')
        rashi = self.cleaned_data.get('rashi')
        horoscope_matching = self.cleaned_data.get('horoscope_matching')

        try:

            new_astological_info_object = ProfileAstrologicalInfo.objects.create(
                gothra=gothra,
                pravara=pravara,
                nakshatra=nakshatra,
                rashi=rashi,
                horoscope_matching=horoscope_matching,
                profile=ProfileBasicInfo.objects.get(id=profile_id)

            )
            return new_astological_info_object

        except Exception as ex:
            print("Profile's Astrological information cannot be updated  because {}".format(ex))
            return False


class ViewAstrologicalInfo(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewAstrologicalInfo, self).__init__(*args, **kwargs)
        astrological_object = ProfileAstrologicalInfo.objects.get(profile_id=profile_object.id)

        self.fields['gothra'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                    initial=astrological_object.gothra)
        self.fields['pravara'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                    initial=astrological_object.pravara)
        self.fields['nakshatra'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                    initial=astrological_object.nakshatra)
        self.fields['rashi'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                    initial=astrological_object.rashi)
        self.fields['horoscope_matching'] = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'readOnly': True}),
                                                    initial=astrological_object.horoscope_matching)


    class Meta:
        model = ProfileAstrologicalInfo
        fields = ('gothra',
                  'pravara',
                  'nakshatra',
                  'rashi',
                  'horoscope_matching'
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

