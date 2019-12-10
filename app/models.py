#  partner - models.py
#
#  Description:
#  Author:           Darshan Nagavara (DN)
#  Created:          13 Nov. 2019
#  Source:           https://github.com/IntersectAustralia/partner
#  License:          Copyright (c) 2019 DN - All Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential
#

#  partner - models.py
#
#

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, User

from django.core.validators import MaxValueValidator


class ProfileBasicInfo(models.Model):
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)
    gender = models.CharField(max_length=40, null=False, blank=False)
    dob = models.DateField(auto_now=False, null=False, blank=False)
    phone_number = models.BigIntegerField(null=False, blank=False, unique=False)
    phone_number_1 = models.CharField(max_length=40, null=True, blank=True)
    phone_number_2 = models.CharField(max_length=40, null=True, blank=True)
    profile_created_by = models.CharField(max_length=40, null=False, blank=False)
    is_active = models.BooleanField(null=True, blank=True,default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProfileBasicInfo, self).save(*args, **kwargs)


class ProfilePersonalInfo(models.Model):
    fathers_name = models.CharField(max_length=40, null=    False, blank=False)
    mothers_name = models.CharField(max_length=40, null=False, blank=False)
    guardians_name= models.CharField(max_length=40, null=False, blank=False)
    fathers_occupation =models.CharField(max_length=40, null=True, blank=True)
    mothers_occupation =models.CharField(max_length=40, null=True, blank=True)
    guardians_occupation = models.CharField(max_length=40, null=True, blank=True)
    resident_of_country= models.CharField(max_length=40, null=False, blank=False)
    resident_of_state = models.CharField(max_length=40, null=False, blank=False)
    resident_of_city_or_village = models.CharField(max_length=40, null=False, blank=False)
    mother_tongue= models.CharField(max_length=40, null=False, blank=False)
    community = models.CharField(max_length=40, null=False, blank=False)
    caste = models.CharField(max_length=40, null=False, blank=False)
    native_place = models.CharField(max_length=40, null=False, blank=False)
    residential_address = models.CharField(max_length=200, null=False, blank=False)
    contact_number = models.BigIntegerField(null=False, blank=False, unique=True)
    additional_info = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField( max_length=100, unique=False)
    profile = models.ForeignKey(ProfileBasicInfo,unique=True, on_delete=models.CASCADE, null=True, blank=True)

    # ToDo: Profile pictures

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProfilePersonalInfo, self).save(*args, **kwargs)


class ProfilePhysicalFeatures(models.Model):
    height = models.CharField(max_length=100, null=True, blank=True)
    body_type = models.CharField(max_length=100, null=False, blank=False)
    complexion=models.CharField(max_length=100, null=False, blank=False)
    physical_status= models.CharField(max_length=100, null=False, blank=False)
    blood_group = models.CharField(max_length=100, null=False, blank=False)
    profile = models.ForeignKey(ProfileBasicInfo, unique=True,on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProfilePhysicalFeatures, self).save(*args, **kwargs)


class ProfileEducationOccupation(models.Model):
    degree_or_diploma = models.CharField(max_length=100, null=True, blank=True)
    pg_degree_or_diploma = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    working_since = models.CharField(max_length=100, null=True, blank=True)
    place_of_occupation = models.CharField(max_length=100, null=True, blank=True)
    average_monthly_income = models.BigIntegerField(null=False, blank=False, unique=True)
    profile = models.ForeignKey(ProfileBasicInfo,unique=True, on_delete=models.CASCADE, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProfileEducationOccupation, self).save(*args, **kwargs)



class ProfileHabits(models.Model):
    food=  models.CharField(max_length=100, null=True, blank=True)
    smoking= models.CharField(max_length=100, null=True, blank=True)
    alcholic_drinks=  models.CharField(max_length=100, null=True, blank=True)
    profile = models.ForeignKey(ProfileBasicInfo,unique=True, on_delete=models.CASCADE, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProfileHabits, self).save(*args, **kwargs)


class ProfileAstrologicalInfo(models.Model):
    gothra = models.CharField(max_length=100, null=True, blank=True)
    pravara = models.CharField(max_length=100, null=True, blank=True)
    nakshatra = models.CharField(max_length=100, null=True, blank=True)
    rashi = models.CharField(max_length=100, null=True, blank=True)
    horoscope_matching = models.CharField(max_length=100, null=True, blank=True)
    profile = models.ForeignKey(ProfileBasicInfo, unique=True,on_delete=models.CASCADE, null=True, blank=True)
    #ToDo: Horoscope upload


    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProfileAstrologicalInfo, self).save(*args, **kwargs)


class ProfileFamilyDetails(models.Model):
    family_class = models.CharField(max_length=100, null=True, blank=True)
    family_type = models.CharField(max_length=100, null=True, blank=True)
    family_values = models.CharField(max_length=100, null=True, blank=True)
    no_of_brothers = models.CharField(max_length=100, null=True, blank=True)
    no_of_sisters = models.CharField(max_length=100, null=True, blank=True)
    married = models.CharField(max_length=100, null=True, blank=True)
    profile = models.ForeignKey(ProfileBasicInfo, unique=True,on_delete=models.CASCADE,  null=True, blank=True)



    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProfileFamilyDetails, self).save(*args, **kwargs)


class ProfileExpectation(models.Model):
    expectations = models.CharField(max_length=10000, null=True, blank=True)
    profile = models.ForeignKey(ProfileBasicInfo, unique=True,on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProfileExpectation, self).save(*args, **kwargs)


class ResetPassword(models.Model):
    reset_password_number = models.BigIntegerField(null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ResetPassword, self).save(*args, **kwargs)


class ProfileImages(models.Model):
    profile_image = models.ImageField(upload_to='media/profile', null=True, blank=True)
    horoscope_image = models.ImageField(upload_to='media/horoscope', null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    profile = models.ForeignKey(ProfileBasicInfo, on_delete=models.CASCADE, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProfileImages, self).save(*args, **kwargs)


class HoroscopeImages(models.Model):
    horoscope_image = models.ImageField(upload_to='media/horoscope', null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    profile = models.ForeignKey(ProfileBasicInfo, on_delete=models.CASCADE, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(HoroscopeImages, self).save(*args, **kwargs)