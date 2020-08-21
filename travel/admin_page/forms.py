from django import forms
from admin_page.models import *
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.forms.widgets import RadioSelect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
import numpy as np



CHOICES=[('ONE WAY', 'One way'),
  ('Round Trip', 'Round Trip')]

################ to bring all dates in list to check avalability ######################

# outStation_dates = OutStation.objects.filter(os_return__gte=timezone.now())
# local_dates = Local.objects.filter(l_return__lte=timezone.now())
# airport_dates = AirPort.objects.filter(ap_return__lte=timezone.now())
# dates = set()
# for x in outStation_dates:
#     xy = x.os_return
#     dates.add("{}-{}-{}".format(xy.year, xy.month, xy.day))
# for x in local_dates:
#     xy = x.l_return
#     dates.add("{}-{}-{}".format(xy.year, xy.month, xy.day))
# for x in airport_dates:
#     xy = x.ap_return
#     dates.add("{}-{}-{}".format(xy.year, xy.month, xy.day))

# dates = list(dates)



class  OutstationForm(ModelForm):
    class Meta:
        model = OutStation
        exclude = ['os_user', 'os_status', 'os_created_on', 'os_updated_on', 'os_order_id', 'os_amount','os_persional_info', 'os_car']
        widgets = {
            #'os_trip_type': RadioSelect(),            
            'os_pickup': DatePicker(),
            'os_picktime': TimePicker(options={
            'format': 'hh:mm A'
            }),
            'os_return': DatePicker(),
            #'os_return': DatePicker(
            #    options={
            #        'disabledDates': dates,
            #    },
            #),
            
        }
    os_trip_type =  forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=(('Round Trip', 'Round Trip'), ('One Way', 'One Way')))
    


class  LocalForm(ModelForm):
    class Meta:
        model = Local
        exclude = ['l_user','l_status', 'l_created_on', 'l_updated_on']
        widgets = {
        'l_pickup': DatePicker(),
        'l_picktime': TimePicker(options={
            'format': 'hh:mm A'
        }),
        'l_return': DatePicker(),

        }

    #l_trip_for =  forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=(('8hrs/100kms', '8 hrs | 100 kms'), ('12hrs/200kms', '12 hrs | 200 kms')))
class  AirPortForm(ModelForm):
    class Meta:
        model = AirPort
        exclude = ['ap_user','ap_status', 'ap_created_on', 'ap_updated_on']
        widgets = {
        'ap_pickup': DatePicker(),
        'ap_picktime': TimePicker(options={
            'format': 'hh:mm A'
        }),
        'ap_return': DatePicker(),

        }
    ap_trip =  forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=(('To The Airport', 'To The Airport'), ('From The Airport', 'From The Airport')))
    
class PersionInfoForm(ModelForm):
    class Meta:
        model = PersionInfo
        exclude = ['p_user', 'p_created_on', 'p_updated_on']

class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['c_user',]
        widgets = {
        'c_car': RadioSelect(),

        }
    c_ac_type =  forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=(('Without Ac', 'W/O AC'),('With Ac', 'WITH AC')))
    #c_car = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check form-check-inline '}), choices=(('zest','ZEST'), ('indica','INDICA'),('Sumo', 'SUMO'),))

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class Cust_SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class CardemoForm(ModelForm):
    class Meta:
        model = Cardemo
        fields = ['cars', 'img', 'ac_price', 'without_ac_price', 'advance']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile 
        exclude = ['user','profile_pic']
        widgets = {
        'date_of_birth': DatePicker(),

        } 