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

#  partner - urls.py
#
#

from django.urls import path

from app.views import index

urlpatterns = [
    # pathj(r'^login/$', index.login, name='login'),
    # path('', user.index, name='login')
    path(r'^/accounts/login/?next=$', index.login, name='login'),
    path('', index.index, name='index'),
    path('login', index.login_view, name='login'),
    path('register', index.register_view, name='register'),
    path('logout', index.logout_view, name='logout'),



]