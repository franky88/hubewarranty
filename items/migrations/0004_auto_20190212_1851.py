# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-12 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_itemname_item_wrty_lngth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemname',
            name='barcode',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='itemname',
            name='item_wrty_lngth',
            field=models.IntegerField(help_text='How many month?', verbose_name='item warranty length'),
        ),
    ]
