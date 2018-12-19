import uuid
from django.db import models
from django.utils import timezone

class Customer(models.Model):
	cid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True) # Customer ID
	name = models.CharField(max_length=128, null=True)
	sex = models.CharField(max_length=128, null=True)
	bithdate = models.DateField(default=timezone.now(), null=True)
	mstatus = models.CharField(max_length=128, null=True)
	phone = models.CharField(max_length=128, null=True)
	email = models.EmailField(null=True)

	def __str__(self):
		return self.name

class Claims(models.Model):
	cid = models.ForeignKey('Customer', on_delete=models.CASCADE)
	dateofclaim = models.DateField(default=timezone.now(), null=True)
	claimhandler = models.ForeignKey('Employee', on_delete=models.CASCADE)
	incident = models.CharField(max_length=128, null=True)

class ClaimSettle(models.Model):
	cid = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
	settlement_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	datesettled = models.DateField(default=timezone.now(), null=True)
	amount = models.DecimalField(max_digits=24, decimal_places=2, null=True)
	settlerid = models.ForeignKey('Employee', on_delete=models.CASCADE)

class Employee(models.Model):
	eid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
	name = models.CharField(max_length=128, null=True)
	dept_name = models.ForeignKey('Departments', on_delete=models.CASCADE)
	designation = models.CharField(max_length=128, null=True)

	def __str__(self):
		return self.name

class Nominees(models.Model):
	cid = models.ForeignKey('Customer', on_delete=models.CASCADE)
	name = models.CharField(max_length=128, null=True)
	relation = models.CharField(max_length=128, null=True)
	sex = models.CharField(max_length=128, null=True)
	phone = models.CharField(max_length=128, null=True)

	def __str__(self):
		return self.name

class Departments(models.Model):
	dname = models.CharField(max_length=128, null=True)
	did = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

	def __str__(self):
		return self.dname