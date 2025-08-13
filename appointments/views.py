from django.shortcuts import render, redirect
from .models import Appointment
from customers.models import Customer
from services.models import Service
from accounts.models import Salon
from django.contrib.auth.decorators import login_required

# @login_required
def list_appointments(request):
    salon = Salon.objects.filter(owner=request.user).first()
    appointments = Appointment.objects.filter(customer__salon=salon) if salon else []
    return render(request, 'appointments/list.html', {'appointments': appointments})

# @login_required
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from accounts.models import Salon
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def add_appointment(request):
    salon = Salon.objects.filter(owner=request.user).first()
    if not salon:
        messages.error(request, "ابتدا سالن خود را ثبت کنید.")
        return redirect('/')
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, salon=salon)
        if form.is_valid():
            form.save()
            messages.success(request, "نوبت با موفقیت ثبت شد.")
            return redirect('list_appointments')
    else:
        form = AppointmentForm(salon=salon)
    
    return render(request, 'appointments/add.html', {'form': form})

