# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-16 23:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0002_remove_project_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 16, 23, 35, 18, 979000, tzinfo=utc)),
        ),
    ]
