from django.contrib import admin

# Register your models here.
from .models import Customer, Claims, ClaimSettle, Employee, Nominees, Departments

admin.site.register(Customer)
admin.site.register(Claims)
admin.site.register(ClaimSettle)
admin.site.register(Employee)
admin.site.register(Nominees)
admin.site.register(Departments)