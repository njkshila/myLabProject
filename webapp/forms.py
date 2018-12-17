from django import forms

class AddCustomer(forms.Form):
	name = forms.CharField(label="name", max_length=128)
	CustomerID = forms.CharField(label="CustomerID", max_length=32)