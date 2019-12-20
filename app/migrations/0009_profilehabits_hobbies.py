#  partner -   0009_profilehabits_hobbies.py
#  Description:
#  Author:           darshan
#  Created:          21 Dec. 2019
#  Source:           https://github.com/dartion/partner
#  License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential

# Generated by Django 2.2 on 2019-12-20 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_profileastrologicalinfo_horoscope_attached'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilehabits',
            name='hobbies',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
