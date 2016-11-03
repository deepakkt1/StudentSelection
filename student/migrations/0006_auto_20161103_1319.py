# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-03 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20161103_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='coverletter',
            field=models.FileField(max_length=255, upload_to='coverletters'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.FileField(max_length=255, upload_to='resumes'),
        ),
    ]
