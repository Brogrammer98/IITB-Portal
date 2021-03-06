# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-11-18 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0025_auto_20171026_0822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField(default=100)),
                ('marks_obtained', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(default='', max_length=500)),
                ('is_subjective', models.BooleanField(default=False)),
                ('option1', models.CharField(default='', max_length=100)),
                ('option2', models.CharField(default='', max_length=100)),
                ('option3', models.CharField(default='', max_length=100)),
                ('option4', models.CharField(default='', max_length=100)),
                ('correct_answer', models.CharField(default='', max_length=20)),
                ('answer_given_by_student', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_attempted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='all_students',
            field=models.ManyToManyField(to='index.Student'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='all_students',
            field=models.ManyToManyField(to='index.Student'),
        ),
        migrations.AddField(
            model_name='question',
            name='parent_quiz',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='index.Quiz'),
        ),
        migrations.AddField(
            model_name='grade',
            name='parent_quiz',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='index.Quiz'),
        ),
        migrations.AddField(
            model_name='grade',
            name='parent_student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='index.Student'),
        ),
    ]
