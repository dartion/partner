
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from app.forms.profile import create_profile_form, personal_info, physical_features, education_occupation, habbits,\
    astrological_info, family_details, expectations
from app.models import ProfileBasicInfo
from django.contrib import messages
from django.shortcuts import render, redirect


@login_required
def create_profile(request):
    form = create_profile_form.CreateProfile(request.POST or None)

    if form.is_valid():
        if form.save(request.user.id):
            return HttpResponse("Profile created successfully")

    return render(request, "profile/basic_info/create_profile_basic_info.html", {"form":form})


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
                return HttpResponse("Profile updated successfully")

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


    return render(request, "profile/basic_info/edit_profile_basic_info.html", {"form":form})


@login_required
def view_profile(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    form = create_profile_form.CreateProfileView(request.POST or None)

    return render(request, "profile/basic_info/view_ profile_basic_info.html", {"form":form})

@login_required
def update_personal_info(request, id=None):
    form = personal_info.UpdateProfilePersonalInfo(request.POST or None)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)
    if id in profile_edit_list:
        form = personal_info.UpdateProfilePersonalInfo(request.POST or None)

        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile creted successfully.")

            return HttpResponse("Profile Personal info updated successfully")
    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed to edit someone else's profile.")
        return redirect('/')
    return render(request, "profile/personal_info/personal_info.html", {"form":form, 'id': profile_object.id})


@login_required
def view_personal_info(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = personal_info.ViewProfilePersonalInfo(request.POST or None, instance=profile_object)
    except Exception as ex:
        return redirect('/')
    return render(request, "profile/basic_info/view_ profile_basic_info.html", {"form":form})

@login_required
def update_physical_features(request, id=None):
    form = physical_features.UpdatePhysicalFeatures(request.POST or None)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)
    if id in profile_edit_list:
        form = physical_features.UpdatePhysicalFeatures(request.POST or None)

        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile's physical details added successfully.")

            return HttpResponse("Profile Personal info updated successfully")
    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed to edit someone else's profile.")
        return redirect('/')
    return render(request, "profile/physical_info/physical_features.html", {"form":form, 'id': profile_object.id})


@login_required
def view_physical_info(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = physical_features.ViewPhysicalFeatures(request.POST or None, instance=profile_object)
    except Exception as ex:
        return redirect('/')
    return render(request, "profile/physical_info/view_physical_features.html", {"form":form})


@login_required
def update_education_occupation(request, id=None):
    form = education_occupation.ProfileEducationOccupation(request.POST or None)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)
    if id in profile_edit_list:
        form = education_occupation.UpdateEducationOccupation(request.POST or None)

        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile's physical details added successfully.")

            return HttpResponse("Profile Personal info updated successfully")
    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed to edit someone else's profile.")
        return redirect('/')
    return render(request, "profile/education_occupation/education_occupation.html", {"form": form, 'id': profile_object.id})


@login_required
def view_edu_occ_info(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = education_occupation.ViewEducationOccupation(request.POST or None, instance=profile_object)
    except Exception as ex:
        return redirect('/')
    return render(request, "profile/physical_info/view_physical_features.html", {"form":form})

@login_required
def update_habbits(request, id=None):
    form = habbits.UpdateHabbits(request.POST or None)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)
    if id in profile_edit_list:
        form = habbits.UpdateHabbits(request.POST or None)

        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile's physical details added successfully.")

            return HttpResponse("Profile Personal info updated successfully")
    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed to edit someone else's profile.")
        return redirect('/')
    return render(request, "profile/education_occupation/education_occupation.html",
                  {"form": form, 'id': profile_object.id})


@login_required
def view_habbits(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = habbits.ViewHabbits(request.POST or None, instance=profile_object)
    except Exception as ex:
        return redirect('/')
    return render(request, "profile/habbits/view_habbits.html", {"form":form})



@login_required
def update_astrological_info(request, id=None):

    form = astrological_info.UpdateAstrologicalInfo(request.POST or None)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)
    if id in profile_edit_list:
        form = astrological_info.UpdateAstrologicalInfo(request.POST or None)

        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile's physical details added successfully.")

            return HttpResponse("Profile Personal info updated successfully")
    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed to edit someone else's profile.")
        return redirect('/')
    return render(request, "profile/education_occupation/education_occupation.html",
                  {"form": form, 'id': profile_object.id})



@login_required
def view_astrological(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = astrological_info.ViewAstrologicalInfo(request.POST or None, instance=profile_object)
    except Exception as ex:
        return redirect('/')
    return render(request, "profile/astrological_info/view_astrological.html", {"form":form})



@login_required
def update_family_details(request, id=None):
    form = family_details.UpdateFamilyDetails(request.POST or None)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)
    if id in profile_edit_list:
        form = family_details.UpdateFamilyDetails(request.POST or None)

        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile's physical details added successfully.")

            return HttpResponse("Profile Personal info updated successfully")
    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed to edit someone else's profile.")
        return redirect('/')
    return render(request, "profile/family_details/family_details.html",
                  {"form": form, 'id': profile_object.id})


@login_required
def view_family_details(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = family_details.ViewFamilyDetails(request.POST or None, instance=profile_object)
    except Exception as ex:
        return redirect('/')
    return render(request, "profile/family_details/view_family_details.html", {"form":form})

@login_required
def update_expectations(request, id=None):
    form = expectations.UpdateExpectations(request.POST or None)
    profile_edit_list = []
    try:
        profile_object = ProfileBasicInfo.objects.get(id=id)
        list = ProfileBasicInfo.objects.filter(user_id=request.user.id)
    except Exception as ex:
        return redirect('/')
    for i in list:
        profile_edit_list.append(i.id)
    if id in profile_edit_list:
        form = expectations.UpdateExpectations(request.POST or None)

        if form.is_valid():
            if form.save(profile_object.id):
                messages.add_message(request, messages.SUCCESS,
                                     "Profile's physical details added successfully.")

            return HttpResponse("Profile Personal info updated successfully")
    else:
        messages.add_message(request, messages.ERROR,
                             "You are not allowed to edit someone else's profile.")
        return redirect('/')
    return render(request, "profile/expectations/expectations.html",
                  {"form": form, 'id': profile_object.id})


@login_required
def view_expectations(request, id):
    profile_object = ProfileBasicInfo.objects.get(id=id)
    try:
        form = expectations.ViewExpectations(request.POST or None, instance=profile_object)

    except Exception as ex:
        return redirect('/')
    return render(request, "profile/expectations/view_expectations.html", {"form":form})
