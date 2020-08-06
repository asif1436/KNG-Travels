"""Travell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home/', views.Home, name='home'),
    #path('autofill/', views.Home, name='autofill'),
    path('checkdate/', views.Check_date, name='checkdate'),
    path('outstation/', views.Oustation_view, name='outstation'),
    path('local/', views.Local_view, name='local'),
    path('airport/', views.Airport_view, name='airport'),
    path('callback/', views.callback, name='callback'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cust/login/', views.login, name='cust_login'),
    path('cust/register/', views.register, name='cust_register'),
    path('accounts/', include('allauth.urls')),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/forgot-password.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/recover-password.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_done.html"),
        name="password_reset_complete"),    
    ]