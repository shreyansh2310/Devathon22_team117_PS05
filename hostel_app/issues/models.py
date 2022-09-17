from asyncio.windows_events import NULL
from decimal import MAX_EMAX
from time import timezone
from tkinter import CASCADE
from django.db import models
import datetime

# Create your models here.
class student_data(models.Model):
    Name=models.CharField(max_length=50,default='xyz')
    mobile=models.CharField(max_length=15)
    regno=models.CharField(max_length=10,primary_key=True)
    roomno=models.CharField(max_length=3)
    floorno=models.CharField(max_length=3)
    block=models.CharField(max_length=2)
    

    def __str__(self):
        return self.regno

    class Meta:
        verbose_name='student_data'


class all_issues(models.Model):
    regno=models.ForeignKey(student_data,on_delete=models.CASCADE)
    type=models.CharField(max_length=20)
    description=models.TextField(max_length=2000)
    upvote=models.CharField(default='1',max_length=10)
    timestamp=models.DateTimeField(auto_now_add=True)
        
    