from django.db import models
from django.contrib.auth.models import User

class Salon(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField(default="آدرس وارد نشده")
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
