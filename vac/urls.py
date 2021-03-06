"""vac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Home.views import *
from Frontend.views import *
from Backend.views import *
from Webversions.views import *

urlpatterns =  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+[
    path('', Home, name = "Home"),
    path('Frontend', FrontendHome, name = "Frontend"),
    path('Backend', Backend, name = "Backend"),
    path('Webversions', Webversions, name = "Webversions"),
    path('Frontend/<str:_Type>/<str:_Title>', Frontend),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
