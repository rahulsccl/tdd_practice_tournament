# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-30 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ib_tournament', '0003_auto_20190129_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='status',
            field=models.CharField(default=b'CAN_JOIN', max_length=50),
        ),
    ]
