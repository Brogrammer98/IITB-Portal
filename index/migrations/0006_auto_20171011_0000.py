# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-10-11 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='_student_courses_+', to='index.student'),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='student',
            name='graduation',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.CharField(default='', max_length=250),
        ),
    ]
