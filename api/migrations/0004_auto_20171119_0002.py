# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 23:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170919_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='weigth',
            new_name='weight',
        ),
    ]