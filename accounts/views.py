from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Salon

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'نام کاربری یا رمز عبور اشتباه است.'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

# @login_required
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Salon.objects.create(owner=user, name=f"سالن {user.username}", address="آدرس وارد نشده")
            messages.success(request, 'حساب شما ایجاد شد! اکنون می‌توانید وارد شوید.')
            return redirect('login')
        else:
            messages.error(request, 'لطفا فرم را به درستی پر کنید.')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
