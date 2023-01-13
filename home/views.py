from http.client import HTTPResponse
from datetime import datetime
from home.models import contact 
from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout

# Create your views here.


def index(request):
    if request.user.is_anonymous:
       return redirect('/login')
   #  return render(request, "index.html")
   
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
      
      Contact = contact(name=name, email=email, phone=phone, city=city)
      Contact.save()
      messages.success(request, 'Your Details Has Been Submitted') 
    return render (request,"contact.html")
# return HttpResponse("This is contact us page")


def services(request):
  return render (request,"services.html")
# return HttpResponse("This is services page")

def cat(request):
   return render (request,"cat.html")
# return HttpResponse(" This Is Cat Section")

def dog(request):
   return render (request,"dog.html")
# return HttpResponse(" This Is Dog Section")

def birds(request):
   return render (request,"birds.html")
# return HttpResponse(" This Is Birds Section")

def other(request):
   return render (request,"other.html")
# return HttpResponse(" Describe Your pet ")



def loginuser(request):
    if request.method=="POST":
        username =request.POST['username']
        password =request.POST['password']
        User = authenticate(username=username, password=password)
        if User is not None:
           login(request, User)
           return redirect('')
           # A backend authenticated the credentials
        else: 
            return render (request,'login.html')
         # No backend authenticated the credentials
        
    return render (request,"login.html")
# return HttpResponse(" This is Your Login page ")


def logoutuser(request):
    logout(request)
    return redirect ('/login')
# return HttpResponse(" This is Your Logout page ")