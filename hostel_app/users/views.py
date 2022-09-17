from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request,'users/login.html')


def logout(request):
    return render(request,'users/logout.html')