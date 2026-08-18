from django.shortcuts import render,redirect
from . models import  registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def register(request):
    if request.method =='POST':
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        user_name=request.POST.get('name')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        if password != cpassword:
            return render(request,'register.html',{'error':'password not match'})
        
        if User.objects.filter(username=user_name).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        user=User.objects.create_user(
            username=user_name,
            email=email,
            password=password
        )
        user.save()

        a=registration(
            user=user,
            full_name=full_name,
            email=email
        )
        a.save()
        
        return redirect('userlogin')
        
    return render(request,'register.html')

def userlogin(request):
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(
            request,
            username=name,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return render(request,'userlogin.html',{'errror':'Invalid user name or password'})

    return render(request,'userlogin.html')

def userlogout(request):
    logout(request)
    return redirect('userlogin')


def setting(request):
    if request.method=='POST':
        old_password=request.POST.get('old_password')
        new_password=request.POST.get('new_password')
        c_password=request.POST.get('new_password2')

        user=request.user
        if not user.check_password(old_password):
            return render(request,'setting.html',{'error':'Incorect password'})
        if new_password != c_password:
            return render(request,'setting.html',{'error':'Password not match'})
        user.set_password(new_password)
        user.save()   
        update_session_auth_hash(request,user)
        return redirect('setting')     
    
    return render(request,'setting.html')

def homepage(request):
    return render(request,'homepage.html')