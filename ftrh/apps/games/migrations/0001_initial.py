# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('linearity', models.IntegerField()),
                ('replayability', models.IntegerField()),
                ('story', models.IntegerField()),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('steamusername', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
