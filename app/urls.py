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

from app.views.Profile import profile_basic_info

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

    # Add Profile
    path('create_profile', profile_basic_info.create_profile, name='create_profile'),
    path('update_personal_info/<int:id>', profile_basic_info.update_personal_info, name='update_personal_info'),
    path('update_physical_features/<int:id>', profile_basic_info.update_physical_features, name='update_physical_features'),
    path('update_education_occupation/<int:id>', profile_basic_info.update_education_occupation, name='update_education_occupation'),
    path('update_habbits/<int:id>', profile_basic_info.update_habbits, name='update_habbits'),
    path('update_astrological_info/<int:id>', profile_basic_info.update_astrological_info, name='update_astrological_info'),
    path('update_family_details/<int:id>', profile_basic_info.update_family_details, name='update_family_details'),
    path('update_expectations/<int:id>', profile_basic_info.update_expectations, name='update_expectations'),

    # Edit Profile
    path('edit_profile/<int:id>', profile_basic_info.edit_profile, name='edit_profile'),

    # View Profile
    path('view_profile/<int:id>', profile_basic_info.view_profile, name='view_profile'),
    path('view_personal_info/<int:id>', profile_basic_info.view_personal_info, name='view_personal_info'),
    path('view_physical_info/<int:id>', profile_basic_info.view_physical_info, name='view_physical_info'),
    path('view_edu_occ_info/<int:id>', profile_basic_info.view_edu_occ_info, name='view_edu_occ_info'),
    path('view_habbits/<int:id>', profile_basic_info.view_habbits, name='view_habbits'),
    path('view_astrological/<int:id>', profile_basic_info.view_astrological, name='view_astrological'),
    path('view_family_details/<int:id>', profile_basic_info.view_family_details, name='view_family_details'),
    path('view_family_details/<int:id>', profile_basic_info.view_family_details, name='view_family_details'),
    path('view_expectations/<int:id>', profile_basic_info.view_expectations, name='view_expectations'),


    # Ajax paths
    path('ajax_get_profile_list/<int:user_id>',index.ajax_get_profile_list, name="ajax_get_profile_list"),

]