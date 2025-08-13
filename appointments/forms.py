from django import forms
from .models import Appointment
from customers.models import Customer
from services.models import Service

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['customer', 'service', 'date', 'amount_paid']

    def __init__(self, *args, **kwargs):
        salon = kwargs.pop('salon', None)
        super().__init__(*args, **kwargs)
        if salon:
            self.fields['customer'].queryset = Customer.objects.filter(salon=salon)
            self.fields['service'].queryset = Service.objects.filter(salon=salon)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
