# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-07-19 05:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PID_app', '0008_auto_20220719_1032'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Employees',
        ),
    ]
