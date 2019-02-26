# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import ItemWarranty, ItemRMA
# Create your views here.
def wrtyList(request):
	item_warranty 		= ItemWarranty.objects.all()
	render_template		= "item_warranty_list.html"
	context				= {
		"title": "list of warranted items",
		"itemwar": item_warranty,
	}
	return render(request, render_template, context)

def wrtyDetail(request, pk):
	instance 			= get_object_or_404(ItemWarranty, pk=pk)
	render_template 	= "item_warranty_detail.html"
	context				= {
		"title": "warranty details",
		"instance": instance,
	}
	return render(request, render_template, context)
