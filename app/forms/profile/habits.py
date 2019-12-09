from django import forms

from app.models import ProfileBasicInfo, ProfileHabits


class UpdateHabits(forms.ModelForm):
    data_exists = False

    def __init__(self, *args, **kwargs):
        profile_id = kwargs.pop('profile_id', None)
        super(UpdateHabits, self).__init__(*args, **kwargs)

        try:

            FOOD_CHOICES = [('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian'),
                            ('Eggetarian', 'Eggetarian')]
            SMOKING_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')]
            ACHOHOLIC_DRINKS_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')]

            habits_object = ProfileHabits.objects.get(profile_id=profile_id)

            self.fields['food'] = forms.CharField(label='Food', widget=forms.Select(
                choices=FOOD_CHOICES, attrs={'class': 'form-control form-control-lg'}), initial=habits_object.food,
                                                  )
            self.fields['smoking'] = forms.CharField(label='Smoking', widget=forms.Select(
                choices=SMOKING_CHOICES, attrs={'class': 'form-control form-control-lg'}),
                                                     initial=habits_object.smoking
                                                     )
            self.fields['alcholic_drinks'] = forms.CharField(label='Alchoholic Drinks', widget=forms.Select(
                choices=ACHOHOLIC_DRINKS_CHOICES, attrs={'class': 'form-control form-control-lg'}),
                                                             initial=habits_object.alcholic_drinks
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
        model = ProfileHabits
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
            p = ProfileHabits.objects.get(profile_id=profile_id)
            p.food = food
            p.smoking = smoking
            p.alcholic_drinks = alcholic_drinks
            p.save()
            return p
        except Exception as e:
            new_habits_object = ProfileHabits.objects.create(
                food=food,
                smoking=smoking,
                alcholic_drinks=alcholic_drinks,
                profile=ProfileBasicInfo.objects.get(id=profile_id)
            )
            return new_habits_object


class ViewHabits(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        profile_object = kwargs.pop('instance', None)
        super(ViewHabits, self).__init__(*args, **kwargs)
        habits_object = ProfileHabits.objects.get(profile_id=profile_object.id)

        FOOD_CHOICES = [('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian'),
                        ('Eggetarian', 'Eggetarian')]
        SMOKING_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')]
        ACHOHOLIC_DRINKS_CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')]


        self.fields['food'] = forms.CharField(widget=forms.Select(choices=FOOD_CHOICES,
                                                                     attrs={'disabled': 'disabled',
                                                                            'class': 'form-control form-control-lg'}),
                                                 initial=habits_object.food)
        self.fields['smoking'] = forms.CharField(widget=forms.Select(choices=SMOKING_CHOICES,
                                                                        attrs={'disabled': 'disabled',
                                                                               'class': 'form-control form-control-lg'}),
                                                    initial=habits_object.smoking)
        self.fields['alcholic_drinks'] = forms.CharField(widget=forms.Select(choices=ACHOHOLIC_DRINKS_CHOICES,
                                                                     attrs={'disabled': 'disabled',
                                                                            'class': 'form-control form-control-lg'}),
                                                 initial=habits_object.alcholic_drinks)

    class Meta:
        model = ProfileHabits
        fields = ('food',
                  'smoking',
                  'alcholic_drinks',
                  )

    def clean(self, *args, **kwargs):
        # ToDo: Clean the input values as required here...
        return self.cleaned_data
