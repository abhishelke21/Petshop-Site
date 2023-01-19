from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.


class contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    city = models.TextField(max_length=12)
    
    
    def __str__(self):
         return self.name
class Product_dog(models.Model):
    name =models.CharField(max_length=225, null=True)
    price = models.FloatField()
    desc = models.TextField()
    digital =models.BooleanField(default=True,null=True,blank=False)
    img = models.ImageField(null=True,blank=False)
    
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url =self.img.url
        except:
            url =''
        return url         
class product_cat(models.Model):
    name =models.CharField(max_length=225, null=True)
    price = models.FloatField()
    desc = models.TextField()
    digital =models.BooleanField(default=True,null=True,blank=False)
    img = models.ImageField(null=True,blank=False)
    
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url =self.img.url
        except:
            url =''
        return url  
class product_bird(models.Model):
    name =models.CharField(max_length=225, null=True)
    price = models.FloatField()
    desc = models.TextField()
    digital =models.BooleanField(default=True,null=True,blank=False)
    img = models.ImageField(null=True,blank=False)
    
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url =self.img.url
        except:
            url =''
        return url  
    


