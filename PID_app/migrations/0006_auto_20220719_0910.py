# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-07-19 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PID_app', '0005_node1_node2_node3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node40',
            fields=[
                ('node_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RenameModel(
            old_name='Node2',
            new_name='Node10',
        ),
        migrations.RenameModel(
            old_name='Node1',
            new_name='Node20',
        ),
        migrations.RenameModel(
            old_name='Node3',
            new_name='Node30',
        ),
    ]