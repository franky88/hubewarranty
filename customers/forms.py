from django import forms
from .models import CustomerName

class CustomerForm(forms.ModelForm):
	class Meta:
		model = CustomerName
		fields = (
				"full_name",
				"contact_number",
				"address",
			)