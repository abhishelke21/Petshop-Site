from django.urls import path , include
from home import views
from django.contrib.auth.decorators import login_required




urlpatterns = [
    path('',views.loginuser, name='loginuser' ),
    path('about',views.about, name='about' ),
    path('contact',views.Contact, name='contact' ),
    path('services',views.services, name='services' ),
    path('cat',views.cat, name='cat' ),
    path('dog',views.dog, name='dog' ),
    path('birds',views.birds, name='birds' ),
    path('other',views.other, name='other' ),
    path('home',views.home, name='home' ),
    path('logout',views.logoutuser, name='logout' ),
    path("register",views.register , name="register")
    ]
    