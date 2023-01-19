from http.client import HTTPResponse
from datetime import datetime
from home.models import contact 
from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
@login_required(login_url="/loginuser")

def home(request):

   

   return render(request,'index.html')
  
   

   # if request.user.is_anonymous:
   #    return render(request, "index.html")
   #    return redirect('/login')
     
   
   
# return ("This is home page")


def about(request):
   
    return render(request, "about.html")
# return HttpResponse("This is about us page")


def Contact(request):
   
    
    if request.method == 'POST':
      name = request.POST.get("name")
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      city = request.POST.get('city')
      
      if contact.objects.filter(name=name, email=email, phone=phone, city=city):
         messages.error(request,"Contact already registered!!")
         return redirect ('/contact')
      
      
      Contact = contact(name=name, email=email, phone=phone, city=city)
      Contact.save()
      messages.success(request, 'Your Details Has Been Submitted') 
    return render (request,"contact.html")
# return HttpResponse("This is contact us page")


def services(request):
   
  return render (request,"services.html")
# return HttpResponse("This is services page")

def cat(request):
   prop = product_cat.objects.all()
   
   return render (request,"cat.html",{'prop':prop})
# return HttpResponse(" This Is Cat Section")

def dog(request):
   prop = Product_dog.objects.all()
   return render (request,"dog.html", {'prop':prop})
# return HttpResponse(" This Is Dog Section")

def birds(request):
   prop = product_bird.objects.all()
   return render (request,"birds.html",{'prop':prop})
# return HttpResponse(" This Is Birds Section")

def other(request):
   return render (request,"other.html")
# return HttpResponse(" Describe Your pet ")



def loginuser(request):
    if request.method=="POST":
        username1 =request.POST['username']
        password1 =request.POST['password']
        User = authenticate(username=username1, password=password1)
        if User is not None:
           login(request, User)
           messages.success(request,"logged in sucessfully")
           return render (request,"index.html")
           # A backend authenticated the credentials
        else: 
            return render (request,'login.html')
         # No backend authenticated the credentials
        
    return render (request,"login.html")
# return HttpResponse(" This is Your Login page ")
def register(request):
   if request.method == 'POST':
      username = request.POST['username']
      
      fname = request.POST['fname']
      lname = request.POST['lname']
      email =request.POST['email']
      password = request.POST['pass1']
      myuser =User.objects.create_user(username,email,password)
      myuser.first_name = fname
      myuser.last_name =lname
      myuser.save()
      messages.success(request,"Your Account has been created sucessfully!! Please log in")
      
      return redirect ('/')
   return render (request,"register.html")

def logoutuser(request):
    logout(request)
    messages.success(request,"Logged out Sucessfully")
    return redirect ('/')
# return HttpResponse(" This is Your Logout page ")