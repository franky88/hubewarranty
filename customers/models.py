# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CustomerName(models.Model):
	full_name 		= models.CharField(max_length=120, null=True, blank=True)
	contact_number	= models.CharField(max_length=15, null=True, blank=True)
	address			= models.TextField(null=True, blank=True)
	timestamp		= models.DateField(auto_now_add=True, auto_now=False)
	updated			= models.DateField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.full_name.upper()