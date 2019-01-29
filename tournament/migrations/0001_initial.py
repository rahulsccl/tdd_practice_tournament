# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-29 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('total_rounds', models.PositiveIntegerField()),
                ('start_datetime', models.DateTimeField()),
            ],
        ),
    ]
