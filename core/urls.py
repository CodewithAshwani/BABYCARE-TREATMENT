from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('',home,name="home"),
    path('about',about_us,name="about"),
    path('team',team,name='team'),
    path('services',services,name="services"),
    path('contact',contact_us,name="contact"),
    path('blog',blog,name="blog"),
    path('schedule_visit',schedule_visit,name="schedule-visit"),
    
]