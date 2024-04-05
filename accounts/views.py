from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'accounts already exists!')
            return redirect('core:home')
        else:
            user = User.objects.filter(username=username).first()
            if user:
                messages.warning(request, 'enter unique username')
                return redirect('accounts:signin') 
            else:
                user = User.objects.create(username=username,password=password)
                login(request,user)
                messages.success(request, 'login successfully!')
                return redirect('core:home')
        
    else:
        return render(request,'registration/signin.html')

def login_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        db_user = User.objects.filter(username = username).first()
        if db_user != None:
            user = authenticate(request,username=username,password=password)
            if user:
                # messages.success(request,'Congratulations! & Welcome! You are successfully login. Now you can fill or edit your profile details & start to find your partner.')
                login(request,db_user)
                # return render(request, 'accounts/successfully-login.html',)
                return redirect("core:home")
            else:
                messages.error(request,'Please make sure you have account!')
                return redirect('accounts:login')
        else:
            messages.error(request,'Please make sure you have account!')
            return redirect('accounts:login')

      
    return render(request,'registration/login.html')   

def logout_view(request):
    logout(request)
    
    return redirect("/")