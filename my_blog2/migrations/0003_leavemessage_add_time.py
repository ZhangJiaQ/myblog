# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 09:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog2', '0002_leavemessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavemessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]
