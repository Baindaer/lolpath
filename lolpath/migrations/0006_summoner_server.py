# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lolpath', '0005_auto_20170614_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='summoner',
            name='server',
            field=models.CharField(default='la1', max_length=64),
            preserve_default=False,
        ),
    ]
