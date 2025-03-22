from django.urls import path
from . import views




urlpatterns = [
    path('', views.indexpage, name='home'),
    path('post/', views.postpage, name='post'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
]
