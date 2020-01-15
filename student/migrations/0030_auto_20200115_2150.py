# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2020-01-15 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0029_mockdatapilot'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilotoffering',
            name='wait_students',
            field=models.ManyToManyField(related_name='waitlisted_students', to='student.Student'),
        ),
        migrations.AlterField(
            model_name='pilotoffering',
            name='day',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='pilotoffering',
            name='enrolment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pilotoffering',
            name='size',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='pilotoffering',
            name='students',
            field=models.ManyToManyField(related_name='enrolled_students', to='student.Student'),
        ),
        migrations.AlterField(
            model_name='pilotoffering',
            name='waitlist',
            field=models.IntegerField(default=0),
        ),
    ]
