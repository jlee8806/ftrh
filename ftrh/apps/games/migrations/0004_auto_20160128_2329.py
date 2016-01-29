# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=b'', width_field='width_field'),
        ),
    ]
