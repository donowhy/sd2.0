# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-03 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='freeSampleSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=300)),
                ('state', models.CharField(blank=True, max_length=300)),
                ('country', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
