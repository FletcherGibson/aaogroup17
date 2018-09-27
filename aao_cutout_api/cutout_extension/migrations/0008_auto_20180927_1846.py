# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-27 08:46
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutout_extension', '0007_auto_20180927_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cutoutquery',
            name='dec',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='Incorrect format. Please try again.', regex='^(?!0\\d|$)\\d*(\\.\\d{1,4})?$')]),
        ),
        migrations.AlterField(
            model_name='cutoutquery',
            name='ra',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='Incorrect format. Please try again.', regex='^(?!0\\d|$)\\d*(\\.\\d{1,4})?$')]),
        ),
    ]
