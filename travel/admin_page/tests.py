from django.test import TestCase
import numpy as np
import pandas as pd
from django.shortcuts import render, redirect , HttpResponseRedirect, reverse, HttpResponse
from admin_page.models import *
#from admin_page.forms import *
#from django.contrib import messages
#from django.core.mail import send_mail, send_mass_mail
#from django.contrib.auth import authenticate, login as auth_login
#from django.conf import settings
#from .models import Transaction
#from django.contrib.auth.models import User
#from .paytm import generate_checksum, verify_checksum
#from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth import authenticate, login
#from django.contrib.auth.decorators import login_required
from django.core import serializers
import numpy as np
from django.utils import timezone
# Create your tests here.

date1 = ['2020-08-01', '2020-08-15', '2020-08-19']
date2 = ['2020-08-02', '2020-08-17', '2020-08-20']

f_date = '2020-08-07'
t_date = '2020-08-16'
# mydates = pd.date_range(date1, date2).tolist()
# print(mydates)
# print(type(mydates))
# if "2020-08-05" in mydates:
#     print("can't book")



# # import datetime
# # date1 = '2011-05-03'
# # date2 = '2011-05-10'
# # start = datetime.datetime.strptime(date1, '%Y-%m-%d')
# # end = datetime.datetime.strptime(date2, '%Y-%m-%d') 
# # step = datetime.timedelta(days=1)
# # li = []
# # while start <= end:
# #     li.append(start.date())
# #     start += step

# # print(li)
# # print(type(li))

# for start, end in date1, date2:
#     print(start, end)
#     if  (start>f_date and end<t_date) or (start<f_date and end>t_date) or (start<t_date and end>t_date) or (start<f_date and end>f_date):
#         print("u can")

# if (12<=20 and 12>=16) and (15<=20 and 15>=16):
# #if (16<=21<=20) and (16<=25<=20):
#     print("u can't ")
# else:
#     print("u can ")

#SELECT os_pickup, os_return, c_car_id FROM admin_page_outstation INNER JOIN admin_page_car ON admin_page_car.id = admin_page_outstation.os_car_id WHERE c_car_id = 1 AND (os_pickup>"" AND `end_date`<".$end_date.") OR (`start_date`<".$start_date." AND `end_date`>".$end_date.") OR (`start_date<".$end_date." AND `end_date`>".$end_date.") OR (`start_date`<".$start_date." AND `end_date`>".$start_date.")");


# subjects=Subject.objects.all()
# obj=Student.objects.filter(id__in=subjects)
# js=serializers.serialize("json",obj)
# return HttpResponse(js)

# cars = Car.objects.all()
# out = OutStation.objects.filter(id__in=cars)
# js=serializers.serialize("json",out)
# HttpResponse(js)

# import requests

# url = "https://www.fast2sms.com/dev/bulk"

# payload = {"sender_id"="FSTSMS",
# "message"="This%20is%20a%20test%20message",
# "language"="english",
# "route"='p',
# "numbers"="9666146101",}
# headers = {
#     'authorization': "F1t5krIUSpe6Vf0mCQ7zZuBJqGcdglhbAMjv9XNToK2PnYRE344HMxXnYkiyDN0wRKlTsFeCaVhZEmjB",
#     'Content-Type': "application/x-www-form-urlencoded",
#     'Cache-Control': "no-cache",
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)