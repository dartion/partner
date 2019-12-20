#!/usr/bin/env python

#  partner -   manage.py
#  Description:
#  Author:           darshan
#  Created:          21 Dec. 2019
#  Source:           https://github.com/dartion/partner
#  License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential

#  partner - manage.py
#
#

#  partner - manage.py
#
#

#  partner - manage.py
#
#

import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'partner.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
