from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class hostel_worker(models.Model):
    userid=models.CharField(max_length=10,default='nitwxyz123')
    name=models.CharField(max_length=50)
    mobile=models.TextField(max_length=20)
    role=models.CharField(max_length=100)
    # expertise=model
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Hostel_worker'
        