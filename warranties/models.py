# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from items.models import ItemName
from customers.models import CustomerName
# Create your models here.
class Remarks(models.Model):
	remarks 			= models.CharField(max_length=120, null=True, blank=True)
	def __str__(self):
		return self.remarks.title()
class ItemWarranty(models.Model):
	item_name 			= models.ForeignKey(ItemName, on_delete=models.CASCADE)
	customer_name		= models.ForeignKey(CustomerName, on_delete=models.CASCADE)
	serial_number		= models.CharField(max_length=60, unique=True)
	timestamp			= models.DateField(auto_now_add=True)
	updated				= models.DateField(auto_now=True)

	def item_warranty_end(self):
		item_wl = self.item_name.item_wrty_lngth
		item_war_lngth = item_wl*30.4375
		war_end = self.timestamp + datetime.timedelta(days=item_war_lngth)
		return war_end
	class Meta:
		verbose_name_plural = "item warranties"

	def item_serial_number(self):
		itemserial = "%s serial no: %s"%(self.item_name, self.serial_number)
		return itemserial

	def warranty_status(self):
		status="Under Warranty"
		end_status="Expired"
		if self.item_warranty_end() >= datetime.date.today():
			return status
		else:
			return end_status

	def __str__(self):
		return self.item_name.itemName().upper()

class ItemRMA(models.Model):
	item_warranty		= models.ForeignKey(ItemWarranty, on_delete=models.CASCADE)
	item_name 			= models.CharField(max_length=120, null=True, blank=True)
	customer_name		= models.CharField(max_length=120, null=True, blank=True)
	serial_number		= models.CharField(max_length=60, unique=True)
	remarks				= models.ForeignKey(Remarks, on_delete=models.CASCADE, default=1)
	timestamp			= models.DateField(auto_now_add=True)
	updated				= models.DateField(auto_now=True)
	def item_warranty_end(self):
		item_wl = self.item_warranty.item_name.item_wrty_lngth
		item_war_lngth = item_wl*30.4375
		war_end = self.item_warranty.timestamp + datetime.timedelta(days=item_war_lngth)
		return war_end
	class Meta:
		verbose_name_plural = "item RMA"
	def __str__(self):
		return self.item_warranty.item_name.itemName().upper()