from django import forms
from admin_page.models import *
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.forms.widgets import RadioSelect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



CHOICES=[('ONE WAY', 'One way'),
  ('Round Trip', 'Round Trip')]
class  OutstationForm(ModelForm):
    class Meta:
        model = OutStation
        exclude = ['os_user', 'os_status', 'os_created_on', 'os_updated_on']
        widgets = {
            #'os_trip_type': RadioSelect(),            
            'os_pickup': DatePicker(),
            'os_return': DatePicker(),
            'os_picktime': TimePicker(),
        }
    
    os_trip_type =  forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=(('Round Trip', 'Round Trip'), ('ONE WAY', 'One way')))
    


class  LocalForm(ModelForm):
    class Meta:
        model = Local
        exclude = ['l_user','l_status', 'l_created_on', 'l_updated_on']
        widgets = {
        'l_pickup': DatePicker(),
        'l_picktime': TimePicker(),

        }

    l_trip_for =  forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=(('8hrs/80kms', '8 hrs | 80 kms'), ('12hrs/120kms', '12 hrs | 120 kms')))
class  AirPortForm(ModelForm):
    class Meta:
        model = AirPort
        exclude = ['ap_user','ap_status', 'ap_created_on', 'ap_updated_on']
        widgets = {
        'ap_pickup': DatePicker(),
        'ap_picktime': TimePicker(),

        }
    ap_trip =  forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=(('CFA', 'From The Airport'), ('CTA', 'To The Airport')))
    
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

    #c_car = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check form-check-inline '}), choices=(('zest','ZEST'), ('indica','INDICA'),('Sumo', 'SUMO'),))


class Student_SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email'] 