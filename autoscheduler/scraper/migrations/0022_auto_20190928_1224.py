# Generated by Django 2.1.7 on 2019-09-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0021_auto_20190928_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='pidm',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
