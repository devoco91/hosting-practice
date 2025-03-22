from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='img')
    date=models.DateTimeField(auto_now_add=True)
    
    
    
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.CharField(max_length=25)
    image=models.ImageField(upload_to='img')
    date=models.DateTimeField(auto_now_add=True)
    
    
    
    
    def __str__(self):
        return self.name
    