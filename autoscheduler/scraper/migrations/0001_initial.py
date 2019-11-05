# Generated by Django 2.2.6 on 2019-11-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dept', models.CharField(db_index=True, max_length=4)),
                ('course_num', models.CharField(db_index=True, max_length=5)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('curr_enrollment', models.IntegerField()),
                ('max_enrollment', models.IntegerField()),
                ('term', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=5)),
                ('description', models.TextField(max_length=100)),
                ('term', models.CharField(max_length=6, null=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=70)),
                ('pidm', models.CharField(max_length=9, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'instructors',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('crn', models.CharField(db_index=True, max_length=10)),
                ('building', models.CharField(max_length=5, null=True)),
                ('meeting_days', models.CharField(max_length=7)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('meeting_type', models.CharField(max_length=50)),
                ('meeting_type_desc', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'meetings',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('subject', models.CharField(db_index=True, max_length=4)),
                ('section_num', models.CharField(db_index=True, max_length=6)),
                ('course_num', models.CharField(db_index=True, max_length=6)),
                ('term_code', models.IntegerField(db_index=True)),
                ('min_credits', models.IntegerField(null=True)),
                ('max_credits', models.IntegerField(null=True)),
                ('max_enrollment', models.IntegerField()),
                ('current_enrolled', models.IntegerField()),
                ('instructor', models.CharField(max_length=100)),
                ('meetings', models.ManyToManyField(to='scraper.Meeting')),
            ],
            options={
                'db_table': 'sections',
            },
        ),
    ]
