# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-18 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20161103_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='classification',
            field=models.CharField(default='CLASS 1', max_length=64),
        ),
    ]