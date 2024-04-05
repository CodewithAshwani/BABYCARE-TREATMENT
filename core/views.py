from django.shortcuts import render,redirect
from .models import Contact,ScheduleVisit
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def team(request):
    return render(request,'team.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        Contact.objects.create(name=name,email=email,mobile_no=mobile,message=message)
        messages.success(request, 'Contact request submitted successfully!')
        return redirect('core:home')
    return render(request,'contact_us.html')

def services(request):
    return render(request,'services.html')

def blog(request):
    return render(request,'blog.html')

def schedule_visit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

        ScheduleVisit.objects.create(name=name,email=email,date=date,time=time,message=message)
        messages.success(request, 'Appointment request submitted successfully!')
        return redirect('core:home')
  
    return render(request,'visit.html')