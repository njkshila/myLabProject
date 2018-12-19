from django.http import HttpResponse, Http404
from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import *

# def user_login(request):
#     context = {}
#     next = request.GET.get('next')
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             if next:
#                 return redirect(next)
#             else:
#                 messages.success(request, "You have successfully logged in!")
#                 return redirect('webapp:home')
#         else:
#             messages.error(request, "Provide valid credentials.")
#             return render(request, 'auth/login.html')
    
#     else:
#         return render(request, 'auth/login.html', context)


# def user_logout(request):
#     messages.success(request, "You have been logged out!")
#     logout(request)
#     return redirect('webapp:login')

# @login_required
def customer(request):
    customerlist = {}
    if request.method == 'POST':
        # Filtered Search
        form = Search(request.POST)
        if form.is_valid():
            if form.cleaned_data['Type'] == 'Name':
                customerlist = Customer.objects.filter(name__icontains=form.cleaned_data['Query'])
            elif form.cleaned_data['Type'] == 'Sex':
                customerlist = Customer.objects.filter(sex__icontains=form.cleaned_data['Query'])
            elif form.cleaned_data['Type'] == 'Date of Birth':
                customerlist = Customer.objects.filter(birthdate__icontains=form.cleaned_data['Query'])
            elif form.cleaned_data['Type'] == 'Marital Status':
                customerlist = Customer.objects.filter(mstatus__icontains=form.cleaned_data['Query'])
            elif form.cleaned_data['Type'] == 'Phone':
                customerlist = Customer.objects.filter(phone__icontains=form.cleaned_data['Query'])
            elif form.cleaned_data['Type'] == 'Email':
                customerlist = Customer.objects.filter(email__icontains=form.cleaned_data['Query'])

        else:
            redirect('webapp:customer')
    else:
        customerlist = Customer.objects.order_by('name')

    if customerlist is None:
        messages.error(request, "No customers exist in the database.")
        return render(request, 'webapp/home/customer.html', {'customerlist' : customerlist} )

    return render(request, 'webapp/home/customer.html', {'customerlist' : customerlist} )

# @login_required
# def add_customer(request):

#     if request.method == 'POST':

#         form = AddCustomer(request.POST)
#         if form.is_valid():
#             cus = Customer(
#                 name=form.cleaned_data['name'],
#                 sex=form.cleaned_data['sex'],
#                 birthdate=form.cleaned_data['birthdate'],
#                 mstatus=form.cleaned_data['mstatus'],
#                 phone=form.cleaned_data['phone'],
#                 email=form.cleaned_data['email'],
#             )
#             cus.save()
#             messages.success(request, "Successfully added a new customer!")
#             return redirect('webapp:customer')
#         else:
#             messages.warning(request, "Couldn't add new customer")
#             return redirect('webapp:customer')

#     else:
#         form = AddCustomer()
#         return render(request, 'webapp/home/add_customer.html', {'form': form})

def employee(request):
    employeelist = {}
    if request.method == 'POST':
        # Filtered Search
        form = Search(request.POST)
        if form.is_valid():
            if form.cleaned_data['Type'] == 'Name':
                employeelist = Employee.objects.filter(name__icontains=form.cleaned_data['Query'])
            elif form.cleaned_data['Type'] == 'Department':
                employeelist = Employee.objects.filter(dept_name__icontains=form.cleaned_data['Query'])
            elif form.cleaned_data['Type'] == 'Designation':
                employeelist = Employee.objects.filter(designation__icontains=form.cleaned_data['Query'])

        else:
            redirect('webapp:employee')
    else:
        employeelist = Employee.objects.order_by('name')

    if employeelist is None:
        messages.error(request, "No employees exist in the database.")
        return render(request, 'webapp/home/employee.html', {'employeelist' : employeelist} )

    return render(request, 'webapp/home/employee.html', {'employeelist' : employeelist} )
