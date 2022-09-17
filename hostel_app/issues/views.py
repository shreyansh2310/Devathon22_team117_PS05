from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'issues/home.html')

def add_issues(request):
    return render(request,'issues/add_issues.html')

def previous_issues(request):
    return render(request,'issues/previous_issues.html')

def worker_login(request):
    return render(request,'isses/workers_login.html')

def check_update(request):
    if request.method=='POST':
        return render(request,'issues/check_update.html')
    return render(request,'issues/check_issues.html')
