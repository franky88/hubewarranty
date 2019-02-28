# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
def image_upload_location(instance, filename):
	return 'item_{0}/{1}'.format(instance.id, filename)
class ItemCategory(models.Model):
	category_name	= models.CharField(max_length=120)
	class Meta:
		verbose_name = "item category"
		verbose_name_plural = "item categories"
	def __str__(self):
		return self.category_name.upper()
class ItemSupply(models.Model):
	supplier_name	= models.CharField(max_length=120, null=True, blank=True)
	supplier_add	= models.TextField(null=True, blank=True)
	supplier_contact = models.CharField(max_length=15, null=True, blank=True)
	timestamp		= models.DateField(auto_now_add=True, auto_now=False)
	updated			= models.DateField(auto_now=True, auto_now_add=False)
	class Meta:
		verbose_name = "item supplier"
		verbose_name_plural = "item suppliers"
	def __str__(self):
		return self.supplier_name.upper()
class ItemName(models.Model):
	barcode			= models.CharField(max_length=120, null=True, blank=True, unique=True)
	item_brand 		= models.CharField(max_length=120)
	item_name		= models.CharField(max_length=120)
	item_model		= models.CharField(max_length=120, null=True, blank=True)
	item_desc		= models.TextField(max_length=120, null=True, blank=True, verbose_name="item description")
	item_photo		= models.ImageField(null=True, blank=True, upload_to=image_upload_location)
	item_wrty_lngth	= models.IntegerField(verbose_name="item warranty length", help_text="How many month?")
	item_cat		= models.ForeignKey(ItemCategory, on_delete=models.CASCADE, verbose_name="item categories", default=1)
	item_supp		= models.ForeignKey(ItemSupply, on_delete=models.CASCADE, verbose_name="item supplier", default=1)
	timestamp		= models.DateField(auto_now_add=True, auto_now=False)
	updated			= models.DateField(auto_now=True, auto_now_add=False)
	class Meta:
		verbose_name = "item name"
		verbose_name_plural = "item names"
	def itemName(self):
		itemname = "%s %s"%(self.item_brand, self.item_name)
		return itemname
	def __str__(self):
		return self.itemName().upper()