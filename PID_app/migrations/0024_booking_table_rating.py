# Generated by Django 3.2 on 2023-03-09 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PID_app', '0023_alter_trip_table_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_table',
            name='Rating',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
