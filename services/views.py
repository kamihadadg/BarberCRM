from django.shortcuts import render, redirect
from .models import Service
from accounts.models import Salon
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm
from django.contrib import messages

@login_required
def list_services(request):
    salon = Salon.objects.filter(owner=request.user).first()
    services = Service.objects.filter(salon=salon) if salon else []
    return render(request, 'services/list.html', {'services': services})

@login_required
def add_service(request):
    salon = Salon.objects.filter(owner=request.user).first()
    if not salon:
        messages.error(request, "ابتدا سالن خود را ثبت کنید.")
        return redirect('/')
    
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.salon = salon
            service.save()
            messages.success(request, "خدمت با موفقیت ثبت شد.")
            return redirect('list_services')
    else:
        form = ServiceForm()
    
    return render(request, 'services/add.html', {'form': form})
