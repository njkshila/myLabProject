from django import forms

# class AddCustomer(forms.Form):
# 	name = forms.CharField(label="Name", max_length=128)
# 	sex = forms.CharField(label="Sex", max_length=128)
# 	bithdate = forms.DateField(label="Birth Date")
# 	mstatus = forms.CharField(label="Marital Status", max_length=128)
# 	phone = forms.CharField(label="Phone", max_length=128)
# 	email = forms.EmailField(label="Email")

# class Claims(forms.Form):
# 	cid = forms.IntegerField(label='Customer ID')
# 	dateofclaim = forms.DateField()
# 	claimhandler = forms.IntegerField(label='Claim Handler ID')
# 	incident = forms.CharField(max_length=128)

# class ClaimSettle(forms.Form):
# 	cid = forms.IntegerField(label='Customer ID')
# 	datesettled = forms.DateField(label='Date of Settlement')
# 	amount = forms.DecimalField(max_digits=24, decimal_places=2)
# 	settlerid = forms.IntegerField(label='Settler ID')

# class Employee(forms.Form):
# 	name = forms.CharField(label='Name')
# 	dept_name = forms.IntegerField(label='Department Name')
# 	designation = forms.CharField(label='Designation')

# class Nominees(forms.Form):
# 	cid = forms.IntegerField(label='Customer ID')
# 	name = forms.CharField(label= 'Name')
# 	relation = forms.CharField(label= 'Relationship To Customer')
# 	sex = forms.CharField(label= 'Sex')
# 	phone = forms.CharField(label= 'Phone Number')

# class Departments(forms.Form):
# 	dname = forms.CharField(label= 'Departmnet Name')

class Search(forms.Form):
    Hidden = forms.CharField(max_length=64)
    Type = forms.CharField(max_length=64)
    Query = forms.CharField(max_length=128)
