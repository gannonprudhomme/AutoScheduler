# Generated by Django 2.1.7 on 2019-09-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0020_auto_20190928_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='pidm',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
