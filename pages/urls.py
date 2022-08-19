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
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.mainpage),
    path('company/',views.company),

    path('MAIN/',views.MAIN),
    path('ABOUTUS/',views.ABOUTUS),
    path('SERVICE/',views.SERVICE),
    path('REVIEW/',views.REVIEW),
    path('QUESTION/',views.QUESTION),
    path('CONTACT/',views.CONTACT),

    path('GOODS/',views.GOODS),
    path('LOGIN/',views.LOGIN),
    path('NEWBE/',views.NEWBE),
]

app_name ='account'
urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='pages/LOGIN.html'), name='로그인'),
    path('logout/', auth_views.LogoutView.as_view(), name='로그아웃'),
]