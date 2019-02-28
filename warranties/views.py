# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ItemWarranty, ItemRMA
from .forms import wrtyForm
# Create your views here.
def wrtyList(request):
	item_warranty 		= ItemWarranty.objects.all().order_by("-timestamp")
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

def wrtyAdd(request):
	form = wrtyForm(request.POST or None, request.FILES or None)
	render_template = "item_warranty_add.html"
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.user=request.user
			instance.save()
			messages.success(request, 'Successfully added.')
			return redirect("warranty:detail", pk=instance.id)
	context = {
		"title": "add item",
		"form": form,
	}
	return render(request, render_template, context)

def wrtyEdit(request, pk):
	instance = get_object_or_404(ItemName, pk=pk)
	form = ItemForm(request.POST or None, request.FILES or None, instance=instance)
	render_template = "item_edit.html"
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request, 'Item successfully updated.')
		return redirect('item:detail', pk=instance.id)
	context = {
		"form": form,
		"title": "edit item",
		"instance": instance,
	}
	return render(request, render_template, context)
