# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20171024_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='graduation',
        ),
        migrations.RemoveField(
            model_name='student',
            name='year',
        ),
        migrations.AlterField(
            model_name='course',
            name='all_students',
            field=models.ManyToManyField(to='index.Student'),
        ),
    ]
