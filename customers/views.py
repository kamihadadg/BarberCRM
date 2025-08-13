from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm
from .models import Customer
from accounts.models import Salon
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def add_customer(request):
    salon = Salon.objects.filter(owner=request.user).first()
    if not salon:
        messages.error(request, "ابتدا سالن خود را ثبت کنید.")
        return redirect('/')
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.salon = salon
            customer.save()
            messages.success(request, "مشتری با موفقیت ثبت شد.")
            return redirect('list_customers')
    else:
        form = CustomerForm()
    
    return render(request, 'customers/add.html', {'form': form})
@login_required
def list_customers(request):
    salon = Salon.objects.filter(owner=request.user).first()
    customers = Customer.objects.filter(salon=salon) if salon else []
    return render(request, 'customers/list.html', {'customers': customers})

