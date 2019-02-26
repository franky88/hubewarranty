# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ItemName, ItemCategory, ItemSupply
# Register your models here.
admin.site.register(ItemName)
admin.site.register(ItemCategory)
admin.site.register(ItemSupply)