# Generated by Django 2.1.7 on 2019-09-28 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0011_auto_20190928_0133'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='department',
            table='departments',
        ),
        migrations.AlterModelTable(
            name='instructor',
            table='instructors',
        ),
    ]
