
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from app.forms.profile import create_profile_form, personal_info, physical_features, education_occupation, habits,\
    astrological_info, family_details, expectations, upload_images
from app.models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from app.models import ProfileImages, HoroscopeImages
from partner.settings import ALLOWED_HOSTS
import json

@login_required
def create_profile(request):
    form = create_profile_form.CreateProfile(request.POST or None)

    if form.is_valid():
        post = form.save(request.user.id)
        messages.add_message(request, messages.SUCCESS,
                             "Profile created successfully.")

        return redirect('/update_personal_info/{}'.format(post.id))

    return render(request, "profile/basic_info/create_profile_basic_info.html", {"form":form, 'profileID':None})


@login_required
def edit_profile(request, id):
    profile = ProfileBasicInfo.objects.get(id=id)
    if profile.submit == True:
        messages.add_message(request, messages.WARNING,
                             "Profile application has been submitted. Please contact administrator to revoke the application.")
        return redirect('/')
    if request.user.is_superuser:
        try:
            profile_object = ProfileBasicInfo.objects.get(id=id)
        except Exception as ex:
            return redirect('/')
        form = create_profile_form.CreateProfileEdit(request.POST or None, instance=profile_object)

        if form.is_valid():
            if form.save(id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile {} updated successfully.".format(profile_object.first_name))
                return render(request, "profile/basic_info/edit_profile_basic_info.html",
                              {"form": form, "profileID": profile_object.id})

    else:
        profile_edit_list = []
        try:
            profile_object = ProfileBasicInfo.objects.get(id=id)
            list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
        except Exception as ex:
            return redirect('/')
        for i in list:
            profile_edit_list.append(i.id)
        if id in profile_edit_list:
            form = create_profile_form.CreateProfileEdit(request.POST or None, instance=profile_object)

            if form.is_valid():
                if form.save(id):
                    return HttpResponse("Profile updated successfully")
        else:
            messages.add_message(request, messages.ERROR,
                                 "You are not allowed to edit someone else's profile.")
            return redirect('/')
    return render(request, "profile/basic_info/edit_profile_basic_info.html", {"form":form, "profileID":profile_object.id})


@login_required
def view_profile(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    form = create_profile_form.CreateProfileView(request.POST or None, instance=profile_object)
    return render(request, "profile/basic_info/view_ profile_basic_info.html", {"form":form, "profileID":profile_object.id})


def update_personal_info_request(request, profile_object):
    form = personal_info.UpdateProfilePersonalInfo(request.POST or None, profile_id=profile_object.id)
    try:
        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile updated successfully.")
            return HttpResponse("Profile Personal info updated successfully")
        print(form.errors)
    except Exception as ex:
        print(ex)

@login_required
def update_personal_info(request, id=None):
    profile = ProfileBasicInfo.objects.get(id=id)
    if profile.submit == True:
        messages.add_message(request, messages.WARNING,
                             "Profile application has been submitted. Please contact administrator to revoke the application.")
        return redirect('/')
    form = personal_info.UpdateProfilePersonalInfo(request.POST or None, profile_id = id)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)

    if request.user.is_superuser:
        update_personal_info_request(request, profile_object)
    else:
        if id in profile_edit_list:
            update_personal_info_request(request, profile_object)
        else:
            messages.add_message(request, messages.ERROR,
                                 "You are not allowed to edit someone else's profile.")
            return redirect('/')
    return render(request, "profile/personal_info/personal_info.html", {"form":form, 'profileID': profile_object.id})



@login_required
def view_personal_info(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = personal_info.ViewProfilePersonalInfo(request.POST or None, instance=profile_object)
    except Exception as ex:
        messages.add_message(request, messages.ERROR,
                             "Profile's Personal information has not been updated yet.")
        return redirect('/view_profile/{}'.format(id))
    return render(request, "profile/personal_info/view_personal_info.html", {"form":form, "profileID":profile_object.id})


def update_physical_features_request(request, profile_object):
    profile = ProfileBasicInfo.objects.get(id=profile_object)
    if profile.submit == True:
        messages.add_message(request, messages.WARNING,
                             "Profile application has been submitted. Please contact administrator to revoke the application.")
        return redirect('/')
    form = physical_features.UpdatePhysicalFeatures(request.POST or None, profile_id=profile_object.id)
    try:
        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile updated successfully.")
            return HttpResponse("Profile Personal info updated successfully")

        else:
            return render(request, "profile/physical_info/physical_features.html",
                          {"form": form, 'profileID': profile_object.id})

    except Exception as ex:
        print(profile_object.id)
        print(ex)

@login_required
def update_physical_features(request, id=None):
    profile = ProfileBasicInfo.objects.get(id=id)
    if profile.submit == True:
        messages.add_message(request, messages.WARNING,
                             "Profile application has been submitted. Please contact administrator to revoke the application.")
        return redirect('/')
    form = physical_features.UpdatePhysicalFeatures(request.POST or None, profile_id=id)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)

    if request.user.is_superuser:
        update_physical_features_request(request, profile_object)
    else:
        if id in profile_edit_list:
            update_physical_features_request(request, profile_object)
        else:
            messages.add_message(request, messages.ERROR,
                                 "You are not allowed to edit someone else's profile.")
            return redirect('/')
    return render(request, "profile/physical_info/physical_features.html", {"form": form, 'profileID': profile_object.id})

@login_required
def view_physical_info(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = physical_features.ViewPhysicalFeatures(request.POST or None, instance=profile_object)
    except Exception as ex:
        messages.add_message(request, messages.ERROR,
                             "Profile's Physical information has not been updated yet.")
        return redirect('/view_profile/{}'.format(id))
    return render(request, "profile/physical_info/view_physical_features.html", {"form":form, "profileID":profile_object.id})


def update_edu_occ_request(request, profile_object):

    form = education_occupation.UpdateEducationOccupation(request.POST or None, profile_id=profile_object.id)
    try:
        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile updated successfully.")
            return HttpResponse("Profile Education and Occupation info updated successfully")
        print(form.errors)
    except Exception as ex:
        print(ex)

@login_required
def update_education_occupation(request, id=None):
    profile = ProfileBasicInfo.objects.get(id=id)
    if profile.submit == True:
        messages.add_message(request, messages.WARNING,
                             "Profile application has been submitted. Please contact administrator to revoke the application.")
        return redirect('/')
    form = education_occupation.UpdateEducationOccupation(request.POST or None, profile_id=id)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)

    if request.user.is_superuser:
        update_edu_occ_request(request, profile_object)
    else:
        if id in profile_edit_list:
            update_edu_occ_request(request, profile_object)
        else:
            messages.add_message(request, messages.ERROR,
                                 "You are not allowed to edit someone else's profile.")
            return redirect('/')
    return render(request, "profile/education_occupation/education_occupation.html", {"form": form, 'profileID': profile_object.id})


@login_required
def view_edu_occ_info(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = education_occupation.ViewEducationOccupation(request.POST or None, instance=profile_object)
    except Exception as ex:
        messages.add_message(request, messages.ERROR,
                             "Profile's Education and Occupation information has not been updated yet.")
        return redirect('/view_profile/{}'.format(id))
    return render(request, "profile/education_occupation/view_education_occupation.html", {"form":form, "profileID":profile_object.id})

def update_habits_request(request, profile_object):
    form = habits.UpdateHabits(request.POST or None, profile_id=profile_object.id)
    try:
        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile updated successfully.")
            return HttpResponse("Profile Habits info updated successfully")
        print(form.errors)
    except Exception as ex:
        print(ex)

@login_required
def update_habits(request, id=None):
    profile = ProfileBasicInfo.objects.get(id=id)
    if profile.submit == True:
        messages.add_message(request, messages.WARNING,
                             "Profile application has been submitted. Please contact administrator to revoke the application.")
        return redirect('/')
    form = habits.UpdateHabits(request.POST or None, profile_id=id)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)

    if request.user.is_superuser:
        update_habits_request(request, profile_object)
    else:
        if id in profile_edit_list:
            update_habits_request(request, profile_object)
        else:
            messages.add_message(request, messages.ERROR,
                                 "You are not allowed to edit someone else's profile.")
            return redirect('/')
    return render(request, "profile/habits/habits.html",
                  {"form": form, 'profileID': profile_object.id})


@login_required
def view_habits(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = habits.ViewHabits(request.POST or None, instance=profile_object)
    except Exception as ex:
        messages.add_message(request, messages.ERROR,
                             "Profile's habits information has not been updated yet.")
        return redirect('/view_profile/{}'.format(id))
    return render(request, "profile/habits/view_habits.html", {"form":form, "profileID":profile_object.id})


def update_astrological_info_request(request, profile_object):
    form = astrological_info.UpdateAstrologicalInfo(request.POST or None, profile_id=profile_object.id)
    try:
        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile updated successfully.")
            return HttpResponse("Profile astrological info updated successfully")
        print(form.errors)
    except Exception as ex:
        print(ex)

@login_required
def update_astrological_info(request, id=None):
    profile = ProfileBasicInfo.objects.get(id=id)
    if profile.submit == True:
        messages.add_message(request, messages.WARNING,
                             "Profile application has been submitted. Please contact administrator to revoke the application.")
        return redirect('/')
    form = astrological_info.UpdateAstrologicalInfo(request.POST or None, profile_id = id)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)

    if request.user.is_superuser:
        update_astrological_info_request(request, profile_object)
    else:
        if id in profile_edit_list:
            update_astrological_info_request(request, profile_object)
        else:
            messages.add_message(request, messages.ERROR,
                                 "You are not allowed to edit someone else's profile.")
    return render(request, "profile/astrological_info/astrological.html", {"form":form, 'profileID': profile_object.id})

@login_required
def view_astrological(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = astrological_info.ViewAstrologicalInfo(request.POST or None, instance=profile_object)
    except Exception as ex:
        messages.add_message(request, messages.ERROR,
                             "Profile's Astrological information has not been updated yet.")
        return redirect('/view_profile/{}'.format(id))
    return render(request, "profile/astrological_info/view_astrological.html", {"form":form, "profileID":profile_object.id})


def update_family_details_request(request, profile_object):
    form = family_details.UpdateFamilyDetails(request.POST or None, profile_id=profile_object.id)
    try:
        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile updated successfully.")
            return HttpResponse("Profile family info updated successfully")
        print(form.errors)
    except Exception as ex:
        print(ex)

@login_required
def update_family_details(request, id=None):
    profile = ProfileBasicInfo.objects.get(id=id)
    if profile.submit == True:
        messages.add_message(request, messages.WARNING,
                             "Profile application has been submitted. Please contact administrator to revoke the application.")
        return redirect('/')
    form = family_details.UpdateFamilyDetails(request.POST or None, profile_id=id)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)

    if request.user.is_superuser:
        update_family_details_request(request, profile_object)
    else:
        if id in profile_edit_list:
            update_family_details_request(request, profile_object)
        else:
            messages.add_message(request, messages.ERROR,
                                 "You are not allowed to edit someone else's profile.")
            return redirect('/')
    return render(request, "profile/family_details/family_details.html", {"form": form, 'profileID': profile_object.id})


@login_required
def view_family_details(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = family_details.ViewFamilyDetails(request.POST or None, instance=profile_object)
    except Exception as ex:
        messages.add_message(request, messages.ERROR,
                             "Profile's Family Details information has not been updated yet.")
        return redirect('/view_profile/{}'.format(id))
    return render(request, "profile/family_details/view_family_details.html", {"form":form, "profileID":profile_object.id})


def update_expectations_request(request, profile_object):
    form = expectations.UpdateExpectations(request.POST or None, profile_id=profile_object.id)
    try:
        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile updated successfully.")
            return HttpResponse("Profile expectations info updated successfully")
        print(form.errors)
    except Exception as ex:
        print(ex)


@login_required
def update_expectations(request, id=None):
    profile = ProfileBasicInfo.objects.get(id=id)
    if profile.submit == True:
        messages.add_message(request, messages.WARNING,
                             "Profile application has been submitted. Please contact administrator to revoke the application.")
        return redirect('/')
    form = expectations.UpdateExpectations(request.POST or None, profile_id=id)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)

    if request.user.is_superuser:
        update_expectations_request(request, profile_object)
    else:
        if id in profile_edit_list:
            update_expectations_request(request, profile_object)
        else:
            messages.add_message(request, messages.ERROR,
                                 "You are not allowed to edit someone else's profile.")
            return redirect('/')
    return render(request, "profile/expectations/expectations.html", {"form": form, 'profileID': profile_object.id})


@login_required
def view_expectations(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = expectations.ViewExpectations(request.POST or None, instance=profile_object)

    except Exception as ex:
        messages.add_message(request, messages.ERROR,
                             "Profile's Expectation information has not been updated yet.")
        return redirect('/view_profile/{}'.format(id))
    return render(request, "profile/expectations/view_expectations.html", {"form":form, "profileID":profile_object.id})


@login_required()
def activate_user(request, profileID):
    if request.user.is_superuser:
        profile_object = ProfileBasicInfo.objects.get(id=profileID)
        profile_object.is_active = True
        profile_object.save()
        messages.add_message(request, messages.SUCCESS,
                             "Profile {} has been activated.".format(
                                 profile_object.first_name + " " + profile_object.last_name))
        return redirect('/')

    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed Activate/Deactivate users")
        return redirect('/')


@login_required()
def deactivate_user(request, profileID):
    if request.user.is_superuser:
        profile_object = ProfileBasicInfo.objects.get(id=profileID)
        profile_object.is_active = False
        profile_object.save()
        messages.add_message(request, messages.WARNING,
                             "Profile {} has been deactivated.".format(profile_object.first_name +" "+ profile_object.last_name))
        return redirect('/')
    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed Activate/Deactivate users")
        return redirect('/')

@login_required()
def delete_profile(request, profileID):
    if request.user.is_superuser:
        profile_object = ProfileBasicInfo.objects.get(id=profileID)
        name = profile_object.first_name+ " " + profile_object.last_name
        profile_object.delete()
        messages.add_message(request, messages.WARNING,
                             "Profile {} has been deleted from the system.".format(
                                 profile_object.first_name + " " + profile_object.last_name))
        return redirect('/')

    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed Activate/Deactivate users")
        return redirect('/')
def update_images_request(request, profile_object):
    form = upload_images.UploadProfileImage(request.POST or None, request.FILES)
    try:
        if form.is_valid():
            if form.save(profile_object):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile image updated successfully.")
            return HttpResponse("Profile expectations info updated successfully")
        print(form.errors)
    except Exception as ex:
        print(ex)

@login_required()
def upload_image(request, profileID):
    form = upload_images.UploadProfileImage(request.POST or None, request.FILES)

    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=profileID)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    try:
        for i in list:
            profile_edit_list.append(i.id)

        if request.user.is_superuser:
            update_images_request(request, profile_object)
        else:
            if profileID in profile_edit_list:
                update_images_request(request, profile_object)
            else:
                messages.add_message(request, messages.ERROR,
                                     "You are not allowed to edit someone else's profile.")
                return redirect('/')
    except Exception as ex:
        print(ex)
    url = ''
    try:
        image_object = ProfileImages.objects.get(profile_id=profile_object.id)
        if image_object.url is not None:
            url = "/"+image_object.url
    except Exception as ex:
        print(ex)
    if len(url) <= 0:
        url = '/media/profile/default_pp.png'


    return render(request, "profile/profile_images/upload_profile_image.html", {"form": form, 'profileID': profile_object.id, 'url':url})


def update_horoscope_images_request(request, profile_object):
    form = upload_images.UploadHoroscopeImage(request.POST or None, request.FILES)
    try:
        if form.is_valid():
            if form.save(profile_object):
                messages.add_message(request, messages.SUCCESS,
                                     "Horoscope image updated successfully.")
            return HttpResponse("Horoscope info updated successfully")
        print(form.errors)
    except Exception as ex:
        print(ex)

@login_required()
def upload_horoscope_image(request, profileID):
    form = upload_images.UploadHoroscopeImage(request.POST or None, request.FILES)

    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=profileID)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    try:
        for i in list:
            profile_edit_list.append(i.id)

        if request.user.is_superuser:
            update_horoscope_images_request(request, profile_object)
        else:
            if profileID in profile_edit_list:
                update_horoscope_images_request(request, profile_object)
            else:
                messages.add_message(request, messages.ERROR,
                                     "You are not allowed to edit someone else's profile.")
                return redirect('/')
    except Exception as ex:
        print(ex)
    url = ''
    try:
        image_object = HoroscopeImages.objects.get(profile_id=profile_object.id)
        if image_object.url is not None:
            url = "/"+image_object.url
    except Exception as ex:
        print(ex)
    if len(url) <= 0:
        url = '/media/profile/default_pp.png'


    return render(request, "profile/profile_images/upload_profile_horoscope.html", {"form": form, 'profileID': profile_object.id, 'url':url})

@login_required
def search_profiles(request):
    try:
        if request.user.is_active:
            return render(request, "menu_content/search_profiles.html")
    except Exception as ex:
        messages.add_message(request, messages.WARNING,
                             "Your profile must first be active to view profiles. Please contanct administrator")
        return redirect('/')


@login_required
def view_profile_image(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        url = "/"+ProfileImages.objects.get(profile_id=profile_object.id).url
    except:
        url = '/media/profile/default_pp.png'

    return render(request, "profile/profile_images/view_profile_image.html",
                  {"url": url, "profileID": profile_object.id})


@login_required
def view_horoscope_image(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        url = "/"+HoroscopeImages.objects.get(profile_id=profile_object.id).url
    except:
        url = '/media/profile/default_pp.png'

    return render(request, "profile/profile_images/view_horoscope_image.html",
                  {"url": url, "profileID": profile_object.id})

@login_required
def ajax_get_all_profile_list(request):
    profile_list = []

    profile_basic_info_object = ProfileBasicInfo.objects.filter(is_active=True)

    try:
        for each_profile in profile_basic_info_object:
            profile_list_dict = {}

            profile_list_dict['dob'] = str(each_profile.dob)
            profile_list_dict['name'] = each_profile.first_name + " " + each_profile.last_name
            profile_list_dict['id'] = each_profile.id
            try:
                profile_list_dict['profile_image'] = "/" + str(ProfileImages.objects.get(profile_id=each_profile.id).url)
            except Exception as ex:
                profile_list_dict['profile_image'] = "/media/profile/default_pp.png"

            try:
                physical_features_object = ProfilePhysicalFeatures.objects.get(profile_id=each_profile.id)
                profile_list_dict['height'] = str(physical_features_object.height)
            except Exception as e:
                profile_list_dict['height'] = "Information not updated by the user"

            try:
                profile_personal_info_object = ProfilePersonalInfo.objects.get(profile_id=each_profile.id)
                profile_list_dict['caste'] = profile_personal_info_object.caste
                profile_list_dict['resident_of_country'] = profile_personal_info_object.resident_of_country

            except Exception as ex:
                profile_list_dict['caste'] = "Information not updated by the user"
                profile_list_dict['resident_of_country'] = "Information not updated by the user"


            profile_list.append(profile_list_dict)

    except Exception as ex:
        print(ex)

    retVal = {"data": profile_list}
    return HttpResponse(json.dumps(retVal), content_type="application/json")

@login_required
def submit_application(request,id):
    same_user = False
    try:
        profile_objects = ProfileBasicInfo.objects.filter(user_id=request.user.id)
        for i in profile_objects:
            if i.id == id:
                same_user = True

    except Exception as ex:
        pass



    try:
        if request.user.is_superuser or same_user:
            user = ProfileBasicInfo.objects.get(id=id)
            user.submit = True
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Your application has been Submitted successfully. Please contact administrator "
                                 "to update your profile")
            return redirect('/')
    except Exception as ex:
        messages.add_message(request, messages.WARNING,
                             "Your profile must first be active to view profiles. Please contanct administrator")
        return redirect('/')

@login_required
def revoke_application(request,id):
    try:
        if request.user.is_superuser:
            user = ProfileBasicInfo.objects.get(id=id)
            user.submit = False
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 "User {} application has been revoked. ".format(user.first_name + " " + user.last_name ))
            return redirect('/')
    except Exception as ex:
        messages.add_message(request, messages.WARNING,
                             "Your profile must first be active to view profiles. Please contanct administrator")
        return redirect('/')