# Generated by Django 3.2 on 2023-03-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PID_app', '0012_auto_20230306_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_reg',
            name='License_image',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='driver_reg',
            name='Status',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='driver_reg',
            name='Vehicle_image',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='driver_reg',
            name='Vehicle_model',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='driver_reg',
            name='Vehicle_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
