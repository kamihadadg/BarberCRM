from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_services, name='list_services'),
    path('add/', views.add_service, name='add_service'),
]
