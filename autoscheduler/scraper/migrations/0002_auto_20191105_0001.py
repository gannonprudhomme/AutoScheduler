# Generated by Django 2.2.6 on 2019-11-05 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='curr_enrollment',
        ),
        migrations.RemoveField(
            model_name='course',
            name='max_enrollment',
        ),
    ]
