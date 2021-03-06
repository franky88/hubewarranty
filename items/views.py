# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ItemName
from .forms import ItemForm
# Create your views here.
def itemList(request):
	item_name = ItemName.objects.all().order_by("-timestamp")
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

def itemAdd(request):
	form = ItemForm(request.POST or None, request.FILES or None)
	render_template = "item_add.html"
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.user=request.user
			instance.save()
			messages.success(request, 'Successfully added.')
			return redirect("item:detail", pk=instance.id)
	context = {
		"title": "add item",
		"form": form,
	}
	return render(request, render_template, context)

def itemEdit(request, pk):
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

def itemDelete(request, pk):
	instance = get_object_or_404(ItemName, pk=pk)
	instance.delete()
	messages.success(request, 'Item successfully deleted.')
	return redirect("item:list")