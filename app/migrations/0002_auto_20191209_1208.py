# Generated by Django 2.2 on 2019-12-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepersonalinfo',
            name='fathers_occupation',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='profilepersonalinfo',
            name='guardians_occupation',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='profilepersonalinfo',
            name='mothers_occupation',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]