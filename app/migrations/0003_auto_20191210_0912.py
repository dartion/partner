#  partner -   0003_auto_20191210_0912.py
#  Description:
#  Author:           darshan
#  Created:          21 Dec. 2019
#  Source:           https://github.com/dartion/partner
#  License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential

# Generated by Django 2.2 on 2019-12-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191209_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepersonalinfo',
            name='residential_address',
            field=models.CharField(max_length=200),
        ),
    ]
