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



