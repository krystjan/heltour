# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_auto_20160717_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('match_count', models.PositiveIntegerField()),
                ('match_points', models.PositiveIntegerField()),
                ('game_points', models.PositiveIntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Team')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='teamscore',
            unique_together=set([('team',)]),
        ),
    ]
