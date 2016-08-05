# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0046_auto_20160802_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='number',
            field=models.PositiveIntegerField(verbose_name='round number'),
        ),
        migrations.AlterField(
            model_name='season',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=255, verbose_name='team name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='number',
            field=models.PositiveIntegerField(verbose_name='team number'),
        ),
    ]