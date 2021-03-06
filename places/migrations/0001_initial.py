# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('latitude', models.IntegerField(default=0)),
                ('longitude', models.IntegerField(default=0)),
                ('facebook', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('site', models.URLField(null=True)),
            ],
        ),
    ]
