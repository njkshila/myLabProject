from django.http import HttpResponse, Http404
from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Customer
from .forms import AddCustomer

def user_login(request):
    context = {}
    next = request.GET.get('next')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if next:
                return redirect(next)
            else:
                messages.success(request, "You have successfully logged in!")
                return redirect('webapp:home')
        else:
            messages.error(request, "Provide valid credentials.")
            return render(request, 'auth/login.html')
    
    else:
        return render(request, 'auth/login.html', context)


def user_logout(request):
    messages.success(request, "You have been logged out!")
    logout(request)
    return redirect('webapp:login')

@login_required
def home(request):
	customer = Customer.objects.order_by('name')
	customerlist = {
		'customer' : customer,
	}

	#if customer is None:
	#	messages.error(request, "No customers exist in the database.")
	#	return render(request, 'webapp/home/home.html', customer)

	return render(request, 'webapp/home/home.html', customerlist)

@login_required
def add_customer(request):

    if request.method == 'POST':

        form = AddCustomer(request.POST)
        if form.is_valid():
            cus = Customer(
                name=form.cleaned_data['Customer Name'],
                CustomerID=form.cleaned_data['CustomerID'],
            )
            cus.save()
            messages.success(request, "Successfully added a new customer!")
            return redirect('webapp:home')
        else:
            messages.warning(request, "Couldn't add new customer")
            return redirect('webapp:home')

    else:
        form = AddCustomer()
        return render(request, 'webapp/home/add_customer.html', {'form': form})