# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-28 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20190226_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemname',
            name='item_desc',
            field=models.TextField(blank=True, max_length=120, null=True, verbose_name='item description'),
        ),
    ]
