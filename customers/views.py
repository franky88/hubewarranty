# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CustomerName
from .forms import CustomerForm
# Create your views here.
def customerList(request):
	customer_name = CustomerName.objects.all().order_by("-timestamp")
	render_template = "customer_list.html"
	context = {
		"title": "customer list",
		"customers": customer_name,
	}
	return render(request, render_template, context)

def customerAdd(request):
	form = CustomerForm(request.POST or None, request.FILES or None)
	render_template = "customer_add.html"
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.user=request.user
			instance.save()
			messages.success(request, 'Successfully added.')
			return redirect("customer:list")
	context = {
		"title": "customer list",
		"form": form,
	}
	return render(request, render_template, context)

def customerDetail(request, pk):
	instance		= get_object_or_404(CustomerName, pk=pk)
	render_template = "customer_detail.html"
	context = {
		"title": "customer detail",
		"instance": instance,
	}
	return render(request, render_template, context)

def customerDelete(request, pk):
	instance = get_object_or_404(CustomerName, pk=pk)
	instance.delete()
	messages.success(request, 'Item successfully deleted.')
	return redirect("customer:list")