# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_hospitalprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalprofile',
            name='ambulance_count',
            field=models.IntegerField(default=0),
        ),
    ]
