# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-18 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20161118_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='project1',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='project2',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='project3',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='project4',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='project5',
            field=models.CharField(max_length=12, null=True),
        ),
    ]