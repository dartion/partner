#  partner -   0008_profileastrologicalinfo_horoscope_attached.py
#  Description:
#  Author:           darshan
#  Created:          21 Dec. 2019
#  Source:           https://github.com/dartion/partner
#  License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
#                    Unauthorized copying of this file, via any medium is
#                    strictly prohibited. Proprietary and confidential

# Generated by Django 2.2 on 2019-12-20 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20191220_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileastrologicalinfo',
            name='horoscope_attached',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]