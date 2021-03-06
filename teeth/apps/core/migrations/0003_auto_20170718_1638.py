# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170716_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
