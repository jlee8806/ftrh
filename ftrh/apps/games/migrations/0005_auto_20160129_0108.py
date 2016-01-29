# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 01:08
from __future__ import unicode_literals

import apps.games.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20160128_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='video',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=apps.games.models.upload_location, width_field='width_field'),
        ),
    ]
