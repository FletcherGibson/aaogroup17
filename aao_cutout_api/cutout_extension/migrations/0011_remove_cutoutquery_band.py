# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-27 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cutout_extension', '0010_auto_20180927_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cutoutquery',
            name='band',
        ),
    ]
