# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-16 22:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='due_date',
        ),
    ]