"""
WSGI config for partner project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

#  partner - wsgi.py
#
#  Description:
#  Author:           Darshan Nagavara (DN)
#  Created:          13 Nov. 2019
#  Source:           https://github.com/IntersectAustralia/partner
#  License:          Copyright (c) 2019 DN - All Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential
#

#  partner - wsgi.py
#
#

#  partner - wsgi.py
#
#

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'partner.settings')

application = get_wsgi_application()
