"""
Copyright (C) 2017 Semester.ly Technologies, LLC

Semester.ly is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Semester.ly is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 15:19


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalTimetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=2)),
                ('time_updated', models.DateTimeField(auto_now_add=True)),
                ('school', models.CharField(max_length=50)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('courses', models.ManyToManyField(to='timetable.Course')),
                ('sections', models.ManyToManyField(to='timetable.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[(b'FIRE', b'FIRE'), (b'LOVE', b'LOVE'), (b'CRAP', b'CRAP'), (b'OKAY', b'OKAY'), (b'BORING', b'BORING'), (b'HARD', b'HARD'), (b'TEARS', b'TEARS'), (b'INTERESTING', b'INTERESTING')], max_length=50)),
                ('course', models.ManyToManyField(to='timetable.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_year', models.CharField(blank=True, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')], max_length=2)),
                ('img_url', models.CharField(default=-1, max_length=300)),
                ('fbook_uid', models.CharField(default=b'', max_length=255)),
                ('gender', models.CharField(default=b'', max_length=255)),
                ('major', models.CharField(default=b'', max_length=255)),
                ('social_courses', models.NullBooleanField()),
                ('social_offerings', models.NullBooleanField()),
                ('friends', models.ManyToManyField(blank=True, related_name='_student_friends_+', to='student.Student')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reaction',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='personaltimetable',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
