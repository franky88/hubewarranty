# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ItemWarranty, ItemRMA, Remarks
# Register your models here.
class ItemWarrantyAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'serial_number', 'customer_name', 'timestamp', 'item_warranty_end')

class ItemRMAAdmin(admin.ModelAdmin):
    list_display = ('__str__','item_name', 'customer_name', 'serial_number', 'timestamp', 'updated')

admin.site.register(ItemWarranty, ItemWarrantyAdmin)
admin.site.register(ItemRMA, ItemRMAAdmin)
admin.site.register(Remarks)