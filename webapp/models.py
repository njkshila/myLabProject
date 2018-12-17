from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=128)
	CustomerID = models.CharField(max_length=32)
