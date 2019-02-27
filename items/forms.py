from django import forms
from .models import ItemName

class ItemForm(forms.ModelForm):
	class Meta:
		model = ItemName
		fields = (
				"barcode",
				"item_brand",
				"item_name",
				"item_model",
				"item_desc",
				"item_photo",
				"item_wrty_lngth",
				"item_cat",
				"item_supp",
			)