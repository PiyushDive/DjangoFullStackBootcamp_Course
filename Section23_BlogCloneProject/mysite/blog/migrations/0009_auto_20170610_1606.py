# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-10 16:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170610_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 10, 16, 6, 52, 6025, tzinfo=utc)),
        ),
    ]