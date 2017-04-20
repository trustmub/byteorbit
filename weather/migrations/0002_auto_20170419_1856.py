# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='max_temp',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='weather',
            name='min_temp',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='weather',
            name='wind_speed',
            field=models.CharField(max_length=255),
        ),
    ]
