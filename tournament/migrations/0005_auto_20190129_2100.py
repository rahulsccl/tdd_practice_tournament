# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-29 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_auto_20190129_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kotournament',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]