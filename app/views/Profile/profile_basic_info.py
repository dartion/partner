
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from app.forms.profile import create_profile_form, personal_info, physical_features, education_occupation, habbits,\
    astrological_info, family_details, expectations, upload_images
from app.models import ProfileBasicInfo
from django.contrib import messages
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from app.models import ProfileImages
from django.urls import reverse_lazy

@login_required
def create_profile(request):
    form = create_profile_form.CreateProfile(request.POST or None)

    if form.is_valid():
        post = form.save(request.user.id)
        return HttpResponse("Profile created successfully")



    return render(request, "profile/basic_info/create_profile_basic_info.html", {"form":form, 'profileID':None})


@login_required
def edit_profile(request, id):
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
                return redirect('/')

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
    form = create_profile_form.CreateProfileView(request.POST or None)
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
        return redirect('/')
    return render(request, "profile/basic_info/view_ profile_basic_info.html", {"form":form, "profileID":profile_object.id})


def update_physical_features_request(request, profile_object):
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
        return redirect('/')
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
        return redirect('/')
    return render(request, "profile/physical_info/view_physical_features.html", {"form":form, "profileID":profile_object.id})

def update_habbits_request(request, profile_object):
    form = habbits.UpdateHabbits(request.POST or None, profile_id=profile_object.id)
    try:
        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile updated successfully.")
            return HttpResponse("Profile Habbits info updated successfully")
        print(form.errors)
    except Exception as ex:
        print(ex)

@login_required
def update_habbits(request, id=None):
    form = habbits.UpdateHabbits(request.POST or None, profile_id=id)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)

    if request.user.is_superuser:
        update_habbits_request(request, profile_object)
    else:
        if id in profile_edit_list:
            update_habbits_request(request, profile_object)
        else:
            messages.add_message(request, messages.ERROR,
                                 "You are not allowed to edit someone else's profile.")
            return redirect('/')
    return render(request, "profile/habbits/habbits.html",
                  {"form": form, 'profileID': profile_object.id})


@login_required
def view_habbits(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = habbits.ViewHabbits(request.POST or None, instance=profile_object)
    except Exception as ex:
        return redirect('/')
    return render(request, "profile/habbits/view_habbits.html", {"form":form, "profileID":profile_object.id})


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
            return redirect('/')
    return render(request, "profile/astrological_info/astrological.html", {"form":form, 'profileID': profile_object.id})

@login_required
def view_astrological(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = astrological_info.ViewAstrologicalInfo(request.POST or None, instance=profile_object)
    except Exception as ex:
        return redirect('/')
    return render(request, "profile/astrological_info/view_astrological.html", {"form":form})


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
        return redirect('/')
    return render(request, "profile/family_details/view_family_details.html", {"form":form})


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
        return redirect('/')
    return render(request, "profile/expectations/view_expectations.html", {"form":form, "profileID":profile_object.id})


@login_required()
def activate_user(request, profileID):
    if request.user.is_superuser:
        profile_object = ProfileBasicInfo.objects.get(id=profileID)
        profile_object.is_active = True
        profile_object.save()
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
        return redirect('/')
    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed Activate/Deactivate users")
        return redirect('/')

@login_required()
def upload_image(request, profileID):
    model = ProfileImages
    p_image = ProfileImages
    try:
        form = upload_images.UploadProfileImage(request.POST or None, request.FILES)
        # form.is_valid()
        if form.is_valid():
            print("All good")
            form.save()
            return HttpResponse("OK")


    except Exception as e:
        print (e)
    template_name = 'profile/profile_images/upload_profile_image.html'
    success_url = reverse_lazy('home')

    return render(request, "profile/profile_images/upload_profile_image.html", {"form": form})


