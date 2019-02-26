# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ItemWarranty, ItemRMA
# Register your models here.
class ItemWarrantyAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'serial_number', 'customer_name', 'timestamp', 'item_warranty_end')

class ItemRMAAdmin(admin.ModelAdmin):
    list_display = ('item_warranty', 'serial_number', 'customer_name', 'remarks', 'item_warranty_end')

admin.site.register(ItemWarranty, ItemWarrantyAdmin)
admin.site.register(ItemRMA, ItemRMAAdmin)