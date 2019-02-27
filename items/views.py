# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import ItemName
from .forms import ItemForm
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

def itemAdd(request):
	form = ItemForm(request.POST or None, request.FILES or None)
	render_template = "item_add.html"
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.user=request.user
			instance.save()
			return redirect("item:detail", pk=instance.id)
	context = {
		"title": "add item",
		"form": form,
	}
	return render(request, render_template, context)