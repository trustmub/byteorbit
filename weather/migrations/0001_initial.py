# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_temp', models.CharField(max_length=25)),
                ('max_temp', models.CharField(max_length=25)),
                ('wind_speed', models.CharField(max_length=25)),
                ('my_date', models.IntegerField()),
                ('rain', models.FloatField()),
                ('summary', models.CharField(max_length=256)),
            ],
        ),
    ]
