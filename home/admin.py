from django.contrib import admin
from home.models import *

# Register your mod.els here.
# admin.site.register(contact)
@admin.register(contact)
class Useradmin(admin.ModelAdmin):
    list_display=('id','name','email','phone','city')
    
@admin.register(Product_dog) 
class Product_dog(admin.ModelAdmin):
    list_display=('id','name','price','desc','digital','img') 
    
     
@admin.register(product_cat) 
class Product_dog(admin.ModelAdmin):
    list_display=('id','name','price','desc','digital','img')
       
@admin.register(product_bird) 
class Product_dog(admin.ModelAdmin):
    list_display=('id','name','price','digital','img')   