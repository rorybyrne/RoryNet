# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='id_string',
            field=models.CharField(default='ronaldtrump', max_length=50),
            preserve_default=False,
        ),
    ]
