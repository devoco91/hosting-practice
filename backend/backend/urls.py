"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "Wazobia Culinary School Administration"
admin.site.site_title = "Wazobia Culinary School Admin Portal"
admin.site.index_title = "Welcome Wazobia Culinary School Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.http_response),
    path('person/', include('person.urls')),
    path('', include('product.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
