from django import forms

from app.models import ProfileBasicInfo, ProfileHabbits


class UpdateHabbits(forms.ModelForm):
    data_exists = False

    def __init__(self, *args, **kwargs):
        profile_id = kwargs.pop('profile_id', None)
        super(UpdateHabbits, self).__init__(*args, **kwargs)

        try:

            FOOD_CHOICES = [('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian'),
                            ('Eggetarian', 'Eggetarian')]
            SMOKING_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')]
            ACHOHOLIC_DRINKS_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')]

            habbits_object = ProfileHabbits.objects.get(profile_id=profile_id)

            self.fields['food'] = forms.CharField(label='Food', widget=forms.Select(
                choices=FOOD_CHOICES, attrs={'class': 'form-control form-control-lg'}), initial=habbits_object.food,
                                                  )
            self.fields['smoking'] = forms.CharField(label='Smoking', widget=forms.Select(
                choices=SMOKING_CHOICES, attrs={'class': 'form-control form-control-lg'}),
                                                     initial=habbits_object.smoking
                                                     )
            self.fields['alcholic_drinks'] = forms.CharField(label='Alchoholic Drinks', widget=forms.Select(
                choices=ACHOHOLIC_DRINKS_CHOICES, attrs={'class': 'form-control form-control-lg'}),
                                                             initial=habbits_object.alcholic_drinks
                                                             )

            data_exists = True

        except Exception as ex:
            print(ex)

    if data_exists == False:
        FOOD_CHOICES = [('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian'),
                        ('Eggetarian', 'Eggetarian')]
        SMOKING_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')]
        ACHOHOLIC_DRINKS_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')]

        food = forms.CharField(label='Food ', widget=forms.Select(choices=FOOD_CHOICES,
                                                                  attrs={'class': 'form-control form-control-lg'}))
        smoking = forms.CharField(label='Smoking', widget=forms.Select(choices=SMOKING_CHOICES,
                                                                       attrs={'class': 'form-control form-control-lg'}))
        alcholic_drinks = forms.CharField(label='Alcoholic Drinks',
                                          widget=forms.Select(choices=ACHOHOLIC_DRINKS_CHOICES,
                                                              attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = ProfileHabbits
        fields = ('food',
                  'smoking',
                  'alcholic_drinks',
                  )

    def clean(self, *args, **kwargs):
        # ToDo: Clean the input values as required here...
        return self.cleaned_data

    def save(self, profile_id, commit=True):

        food = self.cleaned_data.get('food')
        smoking = self.cleaned_data.get('smoking')
        alcholic_drinks = self.cleaned_data.get('alcholic_drinks')

        try:
            p = ProfileHabbits.objects.get(profile_id=profile_id)
            p.food = food
            p.smoking = smoking
            p.alcholic_drinks = alcholic_drinks
            p.save()
            return p
        except Exception as e:
            new_habbits_object = ProfileHabbits.objects.create(
                food=food,
                smoking=smoking,
                alcholic_drinks=alcholic_drinks,
                profile=ProfileBasicInfo.objects.get(id=profile_id)
            )
            return new_habbits_object


class ViewHabbits(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewHabbits, self).__init__(*args, **kwargs)
        habbits_object = ProfileHabbits.objects.get(profile_id=profile_object.id)

        FOOD_CHOICES = [('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian'),
                        ('Eggetarian', 'Eggetarian')]
        SMOKING_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')]
        ACHOHOLIC_DRINKS_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')]


        self.fields['food'] = forms.CharField(widget=forms.Select(choices=FOOD_CHOICES,
                                                                     attrs={'disabled': 'disabled',
                                                                            'class': 'form-control form-control-lg'}),
                                                 initial=habbits_object.food)
        self.fields['smoking'] = forms.CharField(widget=forms.Select(choices=SMOKING_CHOICES,
                                                                        attrs={'disabled': 'disabled',
                                                                               'class': 'form-control form-control-lg'}),
                                                    initial=habbits_object.smoking)
        self.fields['alcholic_drinks'] = forms.CharField(widget=forms.Select(choices=ACHOHOLIC_DRINKS_CHOICES,
                                                                     attrs={'disabled': 'disabled',
                                                                            'class': 'form-control form-control-lg'}),
                                                 initial=habbits_object.alcholic_drinks)

    class Meta:
        model = ProfileHabbits
        fields = ('food',
                  'smoking',
                  'alcholic_drinks',
                  )

    def clean(self, *args, **kwargs):
        # ToDo: Clean the input values as required here...
        return self.cleaned_data
