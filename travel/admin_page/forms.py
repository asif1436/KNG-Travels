from django import forms
from admin_page.models import *
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.forms.widgets import RadioSelect




CHOICES=[('ONE WAY', 'One way'),
  ('Round Trip', 'Round Trip')]
class  OutstationForm(ModelForm):
    class Meta:
        model = OutStation
        exclude = ['os_outstation', 'os_status', 'os_created_on', 'os_updated_on']
        widgets = {
            #'os_trip_type': RadioSelect(),
            'os_car': RadioSelect(),
            'os_pickup': DatePicker(),
            'os_return': DatePicker(),
            'os_picktime': TimePicker(),
        }
    
    os_trip_type =  forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=(('Round Trip', 'Round Trip'), ('ONE WAY', 'One way')))
    


class  LocalForm(ModelForm):
    class Meta:
        model = Local
        exclude = ['l_status', 'l_created_on', 'l_updated_on']
        widgets = {
        'l_pickup': DatePicker(),
        'l_picktime': TimePicker(),

        }

    
class  AirPortForm(ModelForm):
    class Meta:
        model = AirPort
        exclude = ['ap_status', 'ap_created_on', 'ap_updated_on']
        widgets = {
        'ap_pickup': DatePicker(),
        'ap_picktime': TimePicker(),

        }
    
    
class PersionInfoForm(ModelForm):
    class Meta:
        model = PersionInfo
        exclude = ['p_os', 'p_local', 'p_ap', 'p_created_on', 'p_updated_on']

class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['c_os', 'c_local', 'c_ap', 'c_created_on', 'c_updated_on']

    c_car = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'class': 'form-check form-check-inline '}), choices=(('zest','ZEST'), ('indica','INDICA'),('Sumo', 'SUMO'),))