#  partner - urls.py
#
#  Description:
#  Author:           Darshan Nagavara (DN)
#  Created:          13 Nov. 2019
#  Source:           https://github.com/IntersectAustralia/partner
#  License:          Copyright (c) 2019 DN - All Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential
#

#  partner - urls.py
#
#

from django.urls import path

from app.views import index

from app.views.Profile import profile

urlpatterns = [
    # pathj(r'^login/$', index.login, name='login'),
    # path('', user.index, name='login')
    # path(r'^/accounts/login/?next=$', index.login, name='login'),
    path('', index.home, name='index'),

    path('login', index.login_view, name='login'),
    path('register', index.register_view, name='register'),
    path('logout', index.logout_view, name='logout'),
    path ('forgot_password',index.forgot_password, name='forgot_password'),
    path ('reset_password/<int:id>/<int:reset_number>',index.reset_password, name='reset_password'),

    # path ('home_page',index.home_page, name='home_page'),
    path ('about_us',index.about_us, name='about_us'),
    path ('how_to_start',index.how_to_start, name='how_to_start'),
    path ('search_profiles', profile.search_profiles, name='search_profiles'),
    path ('contact_us',index.contact_us, name='contact_us'),

    # Add Profile
    path('create_profile', profile.create_profile, name='create_profile'),
    path('update_personal_info/<int:id>', profile.update_personal_info, name='update_personal_info'),
    path('update_physical_features/<int:id>', profile.update_physical_features, name='update_physical_features'),
    path('update_education_occupation/<int:id>', profile.update_education_occupation, name='update_education_occupation'),
    path('update_habits/<int:id>', profile.update_habits, name='update_habits'),
    path('update_astrological_info/<int:id>', profile.update_astrological_info, name='update_astrological_info'),
    path('update_family_details/<int:id>', profile.update_family_details, name='update_family_details'),
    path('update_expectations/<int:id>', profile.update_expectations, name='update_expectations'),
    path('upload_image/<int:profileID>', profile.upload_image, name='upload_image'),
    path('upload_horoscope_image/<int:profileID>', profile.upload_horoscope_image, name='upload_horoscope_image'),
    path('view_profile_image/<int:id>', profile.view_profile_image, name='view_profile_image'),
    path('view_horoscope_image/<int:id>', profile.view_horoscope_image, name='view_horoscope_image'),

    # Edit Profile
    path('edit_profile/<int:id>', profile.edit_profile, name='edit_profile'),

    # View Profile
    path('view_profile/<int:id>', profile.view_profile, name='view_profile'),
    path('view_personal_info/<int:id>', profile.view_personal_info, name='view_personal_info'),
    path('view_physical_info/<int:id>', profile.view_physical_info, name='view_physical_info'),
    path('view_edu_occ_info/<int:id>', profile.view_edu_occ_info, name='view_edu_occ_info'),
    path('view_habits/<int:id>', profile.view_habits, name='view_habits'),
    path('view_astrological/<int:id>', profile.view_astrological, name='view_astrological'),
    path('view_family_details/<int:id>', profile.view_family_details, name='view_family_details'),
    path('view_family_details/<int:id>', profile.view_family_details, name='view_family_details'),
    path('view_expectations/<int:id>', profile.view_expectations, name='view_expectations'),


    # Ajax paths
    path('ajax_get_profile_list/<int:user_id>',index.ajax_get_profile_list, name="ajax_get_profile_list"),
    path('activate_user/<int:profileID>', profile.activate_user, name="activate_user"),
    path('deactivate_user/<int:profileID>', profile.deactivate_user, name="deactivate_user"),
    path('delete_profile/<int:profileID>', profile.delete_profile, name="delete_profile"),
    path('ajax_get_all_profile_list', profile.ajax_get_all_profile_list, name="ajax_get_all_profile_list"),



]