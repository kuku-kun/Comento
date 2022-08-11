"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from . import views


urlpatterns = [
    path('', views.mainpage),
    path('company/',views.company),
    path('MAIN/',views.MAIN),
    path('ABOUTUS/',views.ABOUTUS),
    path('GOODS/',views.GOODS),
    path('EVENT/',views.EVENT),
    path('QUESTION/',views.QUESTION),
    path('CONTACT/',views.CONTACT),
    path('EVENT_GET/',views.EVENT_P),
]
