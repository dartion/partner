from django import forms
from app.models import ProfileBasicInfo, ProfileAstrologicalInfo

import datetime


class UpdateAstrologicalInfo(forms.ModelForm):
    data_exists = False
    def __init__(self, *args, **kwargs):
        profile_id = kwargs.pop('profile_id', None)
        super(UpdateAstrologicalInfo, self).__init__(*args, **kwargs)
        try:
            astrological_info_object = ProfileAstrologicalInfo.objects.get(profile_id=profile_id)
            self.fields['gothra'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}),
                                                    initial=astrological_info_object.gothra)
            self.fields['pravara'] = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg' }),
                                                     initial=astrological_info_object.pravara,required=False,)
            self.fields['nakshatra'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': True, 'class':'form-control form-control-lg'}),
                initial=astrological_info_object.nakshatra)
            self.fields['rashi'] = forms.CharField(widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg' }),
                                                   initial=astrological_info_object.rashi)
            self.fields['horoscope_matching'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': False, 'class':'form-control form-control-lg'}),
                initial=astrological_info_object.horoscope_matching,required=False)
            self.fields['horoscope_attached'] = forms.CharField(
                widget=forms.TextInput(attrs={'required': False, 'class':'form-control form-control-lg'}),
                initial=astrological_info_object.horoscope_matching,required=False)

            data_exists = True

        except Exception as ex:
            print(ex)
    gothra = forms.CharField(widget=forms.TextInput(attrs={'required': False,'class':'form-control form-control-lg'}))
    pravara = forms.CharField(widget=forms.TextInput(attrs={'required': False,'class':'form-control form-control-lg'}),required=False)
    nakshatra = forms.CharField(widget=forms.TextInput(attrs={'required': False,'class':'form-control form-control-lg'}))
    rashi = forms.CharField(widget=forms.TextInput(attrs={'required': True,'class':'form-control form-control-lg'}))
    horoscope_matching = forms.CharField(widget=forms.TextInput(attrs={'required': False,'class':'form-control form-control-lg'}),required=False)
    horoscope_attached = forms.CharField(widget=forms.TextInput(attrs={'required': False,'class':'form-control form-control-lg'}),required=False)


    class Meta:
        model = ProfileAstrologicalInfo
        fields = ('gothra',
                  # 'pravara',
                  'nakshatra',
                  'rashi',
                  'horoscope_matching',
                  'horoscope_attached',
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
        horoscope_attached = self.cleaned_data.get('horoscope_attached')

        try:
            p = ProfileAstrologicalInfo.objects.get(profile_id=profile_id)
            p.gothra = gothra
            p.pravara = pravara
            p.nakshatra = nakshatra
            p.rashi = rashi
            p.horoscope_matching = horoscope_matching
            p.horoscope_attached = horoscope_attached
            p.save()
            return p
        except Exception as ex:
            new_astological_info_object = ProfileAstrologicalInfo.objects.create(
                gothra=gothra,
                pravara=pravara,
                nakshatra=nakshatra,
                rashi=rashi,
                horoscope_matching=horoscope_matching,
                horoscope_attached=horoscope_attached,
                profile=ProfileBasicInfo.objects.get(id=profile_id)

            )
            return new_astological_info_object


class ViewAstrologicalInfo(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewAstrologicalInfo, self).__init__(*args, **kwargs)
        astrological_object = ProfileAstrologicalInfo.objects.get(profile_id=profile_object.id)

        self.fields['gothra'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=astrological_object.gothra)
        self.fields['pravara'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=astrological_object.pravara)
        self.fields['nakshatra'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=astrological_object.nakshatra)
        self.fields['rashi'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=astrological_object.rashi)
        self.fields['horoscope_matching'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=astrological_object.horoscope_matching)
        self.fields['horoscope_attached'] = forms.CharField(
            widget=forms.TextInput(attrs={'readOnly': True, 'class': 'form-control form-control-lg'}),
            initial=astrological_object.horoscope_attached)

    class Meta:
        model = ProfileAstrologicalInfo
        fields = ('gothra',
                  # 'pravara',
                  'nakshatra',
                  'rashi',
                  'horoscope_matching'
        )

    def clean(self, *args, **kwargs):
        #ToDo: Clean the input values as required here...
        return self.cleaned_data

