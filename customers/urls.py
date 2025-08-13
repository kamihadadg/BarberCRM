from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_customers, name='list_customers'),
    path('add/', views.add_customer, name='add_customer'),

]
