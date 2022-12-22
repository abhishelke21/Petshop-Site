from django.urls import path , include
from home import views

urlpatterns = [
    path('',views.index, name='home' ),
    path('about',views.about, name='about' ),
    path('contact',views.Contact, name='contact' ),
    path('services',views.services, name='services' ),
    path('cat',views.cat, name='cat' ),
    path('dog',views.dog, name='dog' ),
    path('birds',views.birds, name='birds' ),
    path('other',views.other, name='other' ),
    path('login',views.loginuser, name='login' ),
    path('logout',views.logoutuser, name='logout' ),]
    