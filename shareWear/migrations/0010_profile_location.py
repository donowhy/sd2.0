# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareWear', '0009_auto_20170328_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]