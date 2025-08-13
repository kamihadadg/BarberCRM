from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),
    path('customers/', include('customers.urls')),
    path('services/', include('services.urls')),
    path('appointments/', include('appointments.urls')),
    path('', accounts_views.home, name='home'),
    path('accounts/', include('accounts.urls')),

]
