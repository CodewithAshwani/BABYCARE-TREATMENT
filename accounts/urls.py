from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('sign-in/',register,name="signin"),
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    
  
]