from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_appointments, name='list_appointments'),
    path('add/', views.add_appointment, name='add_appointment'),
]
