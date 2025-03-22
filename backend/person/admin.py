from django.contrib import admin
from . models import *

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    
    list_display=('name','email','phone','description','address','image','date')
    
    list_filter=('name','address','date')
    
class ProductAdmin(admin.ModelAdmin):
    
    list_display=('name','price','image','date')
    
    list_filter=('name','date')



admin.site.register(Profile,ProfileAdmin)
admin.site.register(Product,ProductAdmin)
