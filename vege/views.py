from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def receipes(request):
    if request.method == "POST":  # Fix: should be uppercase "POST"
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(receipe_image=receipe_image,receipe_name=receipe_name,receipe_description=receipe_description,
                               )
        return redirect('/receipes/') 
    queryset=Receipe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context={'receipes':queryset}
        # print(receipe_name)
        # print(receipe_description)
        # print(receipe_image)

    return render(request, 'receipes.html',context)


def delete_receipe(request,id):
    # print(id)
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    
    return redirect('/receipes/')
    
    # return HttpResponse("a")


def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method =="POST":
        data=request.POST
        
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect('/receipes/')
   
    context={'receipe':queryset}
    
    return render(request,'update_receipes.html',context)

def login_page(request):
    
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/receipes/')
        
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/') 

def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request,"Username already exists")
            return redirect('/register/')
        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        messages.success(request,"User created successfully")
        return redirect('/register/')
    return render(request,'register.html')