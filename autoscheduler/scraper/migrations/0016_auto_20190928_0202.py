# Generated by Django 2.1.7 on 2019-09-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0015_auto_20190928_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='max_credits',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='min_credits',
            field=models.IntegerField(null=True),
        ),
    ]
