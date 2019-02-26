# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import ItemName
# Create your views here.
def itemList(request):
	item_name = ItemName.objects.all()
	render_template = "item_list.html"
	context = {
		"title": "item with warranties",
		"itemname": item_name,
	}
	return render(request, render_template, context)

def itemDetail(request, pk):
	instance		= get_object_or_404(ItemName, pk=pk)
	render_template = "item_detail.html"
	context = {
		"title": "item detail",
		"instance": instance,
	}
	return render(request, render_template, context)