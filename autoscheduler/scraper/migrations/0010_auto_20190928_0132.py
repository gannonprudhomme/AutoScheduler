# Generated by Django 2.1.7 on 2019-09-28 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0009_auto_20190928_0005'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='meeting',
            table='meeting',
        ),
        migrations.AlterModelTable(
            name='section',
            table='section',
        ),
    ]
