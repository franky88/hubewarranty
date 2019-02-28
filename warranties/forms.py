from django import forms
from .models import ItemWarranty, ItemRMA, Remarks

class wrtyForm(forms.ModelForm):
	class Meta:
		model = ItemWarranty
		fields = (
				"item_name",
				"customer_name",
				"serial_number",
			)