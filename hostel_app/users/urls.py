from django.contrib import admin
from django.urls import path,include
from . import views as users

urlpatterns = [
    path('login/',users.login,name="login"),
    path('logout/',users.logout,name="logout"),
    # path('user/',include('users.urls'),name='user_page'),
]
