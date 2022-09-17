from django.contrib import admin
from django.urls import path,include
from . import views as issue

urlpatterns = [
    path('',issue.home,name="home"),
    path('check_update/',issue.check_update,name="check_update"),
    path('add_issues/',issue.add_issues,name="add_issues"),
    path('previous/',issue.previous_issues,name="previous_issues"),
    path('worker_login/',issue.worker_login,name="worker_login"),
    
    # path('user/',include('users.urls'),name='user_page'),
]
