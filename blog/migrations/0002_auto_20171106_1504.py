# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
