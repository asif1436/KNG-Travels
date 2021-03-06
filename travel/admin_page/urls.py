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
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    #path('autofill/', views.Home, name='autofill'),
    path('checkdate/', views.Check_date, name='checkdate'),
    path('offline/', views.base_layout, name='offline'),
    path('profile/', views.Profile_view, name='profile'),
    path('upcoming/', views.Live_Bookings, name='upcoming'),
    path('cancelbooking/<int:c_id>/', views.Cancel_Booking, name='cancelbooking'),
    path('editbooking/<int:c_id>/', views.Edit_Booking, name='editbooking'),
    path('outstation/', views.Oustation_view, name='outstation'),
    path('local/', views.Local_view, name='local'),
    path('airport/', views.Airport_view, name='airport'),
    path('callback/', views.callback, name='callback'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cust/login/', views.login, name='cust_login'),
    path('cust/register/', views.register, name='cust_register'),
    path('accounts/', include('allauth.urls')),
    path('autocomplete/', views.Autocomplete, name='autocomplete'),
    path('autocomplete-airport/', views.Autocomplete_airport, name='autocomplete_airport'),
    path('live-booking/', views.AdminLiveBook, name='live_booking'),
    path('pre-booking/', views.AdminPreBook, name='pre_booking'),
    path('add-car/', views.Addcar, name='add_car'),
    path('view-car/<int:c_id>/', views.Editcar, name='edit_car'),
    path('delete-car/<int:c_id>/', views.Deletecar, name='delete_car'),
    path('car-details/', views.Cardetail, name='car_detail'),
    path('add-cities/', views.Add_Cities, name='add_cities'),
    path('privacy-policy/', views.Privacy_Policy, name='privacy_policy'),
    path('terms-conditions/', views.Terms_Conditions, name='terms_conditions'),

    path('outstationlive_view/', views.Oustation_live_view, name='outstationlive_view'),
    path('locallive_view/', views.Local_live_view, name='locallive_view'),
    path('airportlive_view/', views.Airport_live_view, name='airportlive_view'),

    path('outstationpre_view/', views.Oustation_pre_view, name='outstationpre_view'),
    path('localpre_view/', views.Local_pre_view, name='localpre_view'),
    path('airportpre_view/', views.Airport_pre_view, name='airportpre_view'),
    

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

    path('password_change/', views.change_password, name="password_change"),
    path('kng-download/', views.download_apk, name='kng_download'),    
    ]