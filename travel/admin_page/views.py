import requests
from django.shortcuts import render, redirect , HttpResponseRedirect, reverse, HttpResponse
from admin_page.models import *
from admin_page.forms import *
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
#from .models import Transaction
from django.contrib.auth.models import User
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
import numpy as np
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from admin_page.decorators import Admin_only, User_only

# Create your views here.

def base_layout(request):
	template='base.html'
	return render(request,template)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username__iexact=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('cust/login/')



def register(request):
    if request.method == "POST":
        signup = Cust_SignUpForm(request.POST)
        if signup.is_valid():
            signup.save()
            return redirect('/')
    signup = Cust_SignUpForm()
    return render(request, 'register.html', {'signup': signup})
@User_only
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'registration/change_password.html', {'form': form})

@login_required

def Home(request):
    if request.method == "POST":
        advance = float(request.POST['amount'])
        os_form = OutstationForm(request.POST )
        l_form= LocalForm(request.POST)
        ap_form = AirPortForm(request.POST)
        car_form = CarForm(request.POST)
        pi_form = PersionInfoForm(request.POST)
        if os_form.data["os_from"]:
            if os_form.is_valid() and car_form.is_valid() and pi_form.is_valid():

                car_data = car_form.cleaned_data
                cr = car_form.save(commit=False)
                cr.c_user = request.user
                cr.c_advance = advance
                
                
                pi_data = pi_form.cleaned_data                
                pi = pi_form.save(commit=False)
                pi.p_user = request.user
                

                os_data = os_form.cleaned_data             
                os = os_form.save(commit=False)
                os.os_user = request.user
                os.os_car = cr
                os.os_persional_info = pi

                ############  saving data ##########
                pi.save()
                if pi.p_order_id is None and pi.p_created_on and pi.id:
                    pi.p_order_id = pi.p_created_on.strftime('KNG%Y%m%dODR') + str(pi.id)
                    pi.save()
                cr.save()
                os.save()

                ########## email gateway ############

                message1 = ('New Booking', 'Dear ' + pi_data['p_name'] +',\nThank You for Booking With KNG Travles. \nYour Booking ID: '+ pi.p_order_id + ' You booked a '+ str(car_data['c_car']) +  ' '+ car_data['c_ac_type'] + ' for ' + os_data['os_from'] + ' to ' + os_data['os_to'] + ', on '+ str(os_data['os_pickup']) +' at '+ str(os_data['os_picktime'])+'. \nWe wish you a very happy and safe Journey, \nIf you have any query contact on 9666817780 .' , settings.EMAIL_HOST_USER, [pi_data['p_email'],])
                message2 = ('New Booking', 'Dear Nithish, \nYour '+ str(car_data['c_car']) +  ' '+ car_data['c_ac_type']+ ' Booked for ' + os_data['os_from'] + ' to ' + os_data['os_to'] + ' on '+ str(os_data['os_pickup']) +' at '+ str(os_data['os_picktime'])+'. \nHis Name : ' + pi_data['p_name'] + ' Contact No : ' + pi_data['p_Phone'] + ' and Mail id : ' + pi_data['p_email'] + '.', settings.EMAIL_HOST_USER, ['kondanithishgoud1436@gmail.com',])
                send_mass_mail((message1, message2), fail_silently=False)
                
                ######### sms gatway ###########

                url = "https://www.fast2sms.com/dev/bulk"

                text_message = ('Dear ' + pi_data['p_name'] +',\nThank You for Booking With KNG Travels. \nYour Booking ID: '+ pi.p_order_id + '.\nIf you have any query contact on 9666817780.')
                print(text_message)
                payload1 = {"sender_id":"FSTSMS",
                    "message":text_message,
                    "language":"english",
                    "route":'p',
                    "numbers": pi_data['p_Phone'],
                    }
                text_sms = ('Dear Nithish,\nYour '+str(car_data['c_car'])+' Booked for ' + os_data['os_from'].split(',')[0] + ' to ' + os_data['os_to'].split(',')[0] + ' on '+ str(os_data['os_pickup']) +' '+ os_data['os_picktime'] +'. \nHis Name: ' + pi_data['p_name'] +' & P.No: ' +pi_data['p_Phone']+'.')
                print(text_sms)
                payload2 = {"sender_id":"FSTSMS",
                    "message":text_sms,
                    "language":"english",
                    "route":'p',
                    "numbers":"9666817780",
                    }
                headers = {
                    'authorization': "F1t5krIUSpe6Vf0mCQ7zZuBJqGcdglhbAMjv9XNToK2PnYRE344HMxXnYkiyDN0wRKlTsFeCaVhZEmjB",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                    }

                response = requests.request("POST", url, data=payload1, headers=headers)
                response = requests.request("POST", url, data=payload2, headers=headers)

                #print(response.text)
                

                ########### redirect with data #############
                context = {
                    "order_id" : pi.p_order_id,
                    'name' : request.user.username,
                    'os_data' : os_data,
                    'pi_data' : pi_data,
                    'car_data' : car_data,
                    'advance' : advance,
                    'balance' : car_data['c_amount']-advance,
                }

                return render(request, 'thankq.html', context)

            else:
                messages.error(request, 'Somthing went Wrong!', extra_tags='red')
                return redirect('/')

        elif l_form.data["l_from"]:
            print('local')
            if car_form.is_valid() and l_form.is_valid() and pi_form.is_valid():
                
                car_data = car_form.cleaned_data
                cr = car_form.save(commit=False)
                cr.c_user = request.user
                cr.c_advance = advance

                                
                pi_data = pi_form.cleaned_data
                pi = pi_form.save(commit=False)
                pi.p_user = request.user


                l_data = l_form.cleaned_data
                l = l_form.save(commit=False)
                l.l_user = request.user
                l.l_car = cr
                l.l_persional_info = pi

                # ///// saving Data /////
                pi.save()
                if pi.p_order_id is None and pi.p_created_on and pi.id:
                    pi.p_order_id = pi.p_created_on.strftime('KNG%Y%m%dODR') + str(pi.id)
                    pi.save()
                cr.save()
                l.save()


                # ///// send mail /////

                message1 = ('New Booking', 'Dear ' + pi_data['p_name'] +',\nThank You for Booking With KNG Travles. \nYour ID: '+ pi.p_order_id + ' You booked a '+ str(car_data['c_car'])+ ' '+ car_data['c_ac_type'] + ' for ' + l_data['l_from'] + ' to ' + l_data['l_to'] + ', on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \nWe wish you a very happy and safe Journey, \nIf you have any query contact on 9666817780 .' , settings.EMAIL_HOST_USER, [pi_data['p_email'],])
                message2 = ('New Booking', 'Dear Nithish, \nYour '+ str(car_data['c_car'])+ ' '+ car_data['c_ac_type'] + ' Booked for ' + l_data['l_from'] +' to ' + l_data['l_to'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \nHis Name : ' + pi_data['p_name']+ ' Contact No : ' + pi_data['p_Phone'] + ' and Mail id ' + pi_data['p_email'] + '.', settings.EMAIL_HOST_USER, ['kondanithishgoud1436@gmail.com',])
                send_mass_mail((message1, message2), fail_silently=False)

                ######### sms gatway ###########

                url = "https://www.fast2sms.com/dev/bulk"

                text_message = ('Dear ' + pi_data['p_name'] +',\nThank You for Booking With KNG Travels. \nYour Booking ID: '+ pi.p_order_id + '.\nIf you have any query contact on 9666817780.')
                print(text_message)
                payload1 = {"sender_id":"FSTSMS",
                    "message":text_message,
                    "language":"english",
                    "route":'p',
                    "numbers": pi_data['p_Phone'],
                    }
                text_sms = ('Dear Nithish,\nYour '+str(car_data['c_car'])+' Booked for ' + l_data['l_from'].split(',')[0] + ' to ' + l_data['l_to'].split(',')[0] + ' on '+ str(l_data['l_pickup']) +' '+ l_data['l_picktime'] +'. \nHis Name: ' + pi_data['p_name'] +' & P.No : ' +pi_data['p_Phone']+'.')
                print(text_sms)
                payload2 = {"sender_id":"FSTSMS",
                    "message":text_sms,
                    "language":"english",
                    "route":'p',
                    "numbers":"9666817780",
                    }
                headers = {
                    'authorization': "F1t5krIUSpe6Vf0mCQ7zZuBJqGcdglhbAMjv9XNToK2PnYRE344HMxXnYkiyDN0wRKlTsFeCaVhZEmjB",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                    }

                response = requests.request("POST", url, data=payload1, headers=headers)
                response = requests.request("POST", url, data=payload2, headers=headers)

                # ///// redirecting with data /////
                context = {
                    "order_id" : pi.p_order_id,
                    'name' : request.user.username,
                    'l_data' : l_data,
                    'pi_data' : pi_data,
                    'car_data' : car_data,
                    'advance' : advance,
                    'balance' : car_data['c_amount']-advance,
                }

                return render(request, 'thankq.html', context)
            
            else:
                messages.error(request, 'Somthing went Wrong!', extra_tags='red')
                return redirect('/')

        elif ap_form.data["ap_city"]:
            if ap_form.is_valid() and car_form.is_valid() and pi_form.is_valid():

                
                car_data = car_form.cleaned_data
                cr = car_form.save(commit=False)
                cr.c_user = request.user
                cr.c_advance = advance

                
                pi_data = pi_form.cleaned_data                
                pi = pi_form.save(commit=False)
                pi.p_user = request.user


                ap_data = ap_form.cleaned_data                
                ap = ap_form.save(commit=False)
                ap.ap_user = request.user
                ap.ap_car = cr
                ap.ap_persional_info = pi
                
                
                # ///// DATA Save //////
                pi.save()
                if pi.p_order_id is None and pi.p_created_on and pi.id:
                    pi.p_order_id = pi.p_created_on.strftime('KNG%Y%m%dODR') + str(pi.id)
                    pi.save()
                cr.save()
                ap.save()

                #/////// emial sending ////////
                message1 = ('New Booking', 'Dear ' + pi_data['p_name'] +',\nThank You for Booking With KNG Travles. \nYour ID: '+  pi.p_order_id + ' You booked a '+ str(car_data['c_car']) + ' '+ car_data['c_ac_type']+ ' for ' + ap_data['ap_city'] + ' to ' + ap_data['ap_pic_add'] + ', on '+ str(ap_data['ap_pickup']) +' at '+ str(ap_data['ap_picktime'])+'. \nWe wish you a very happy and safe Journey, \nIf you have any query contact on 9666817780 .' , settings.EMAIL_HOST_USER, [pi_data['p_email'],])
                message2 = ('New Booking', 'Dear Nithish, \nYour '+ str(car_data['c_car']) + ' '+ car_data['c_ac_type']+ ' Booked for '+ ap_data['ap_city']+' to ' + ap_data['ap_pic_add'] +' on '+ str(ap_data['ap_pickup']) +' at '+ str(ap_data['ap_picktime'])+'. \nHis Name : ' + pi_data['p_name']+' Contact No : ' + pi_data['p_Phone'] + ', and Mail id ' + pi_data['p_email'] + '.', settings.EMAIL_HOST_USER, ['kondanithishgoud1436@gmail.com',])
                send_mass_mail((message1, message2), fail_silently=False)

                ######### sms gatway ###########

                url = "https://www.fast2sms.com/dev/bulk"

                text_message = ('Dear ' + pi_data['p_name'] +',\nThank You for Booking With KNG Travels. \nYour Booking ID: '+ pi.p_order_id + '.\nIf you have any query contact on 9666817780.')
                print(text_message)
                payload1 = {"sender_id":"FSTSMS",
                    "message":text_message,
                    "language":"english",
                    "route":'p',
                    "numbers": pi_data['p_Phone'],
                    }
                text_sms = ('Dear Nithish,\nYour '+str(car_data['c_car'])+' Booked for ' + ap_data['ap_city'].split(',')[0] + ' to ' + ap_data['ap_pic_add'].split(',')[0] +' on '+ str(ap_data['ap_pickup']) +' '+ ap_data['ap_picktime'] +'.\nHis Name: ' + pi_data['p_name'] +' & P.No: ' +pi_data['p_Phone']+'.')
                print(text_sms)
                payload2 = {"sender_id":"FSTSMS",
                    "message":text_sms,
                    "language":"english",
                    "route":'p',
                    "numbers":"9666817780",
                    }
                headers = {
                    'authorization': "F1t5krIUSpe6Vf0mCQ7zZuBJqGcdglhbAMjv9XNToK2PnYRE344HMxXnYkiyDN0wRKlTsFeCaVhZEmjB",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                    }

                response = requests.request("POST", url, data=payload1, headers=headers)
                response = requests.request("POST", url, data=payload2, headers=headers)


                # ////// redirect with data ///////

                context = {
                    "order_id" : pi.p_order_id,
                    'name' : request.user.username,
                    'ap_data' : ap_data,
                    'pi_data' : pi_data,
                    'car_data' : car_data,
                    'advance' : advance,
                    'balance' : (car_data['c_amount'])-advance,
                }

                return render(request, 'thankq.html', context)
       
                   
            else:
                messages.error(request, 'Somthing went Wrong!', extra_tags='red')
                return redirect('/')
    else:
        car_data = Cardemo.objects.all()
        #car_json = serializers.serialize("json",  Cardemo.objects.all())
        json_serializer = serializers.get_serializer("json")()
        companies = json_serializer.serialize(Cardemo.objects.all(), ensure_ascii=False)
       
        context = {
            'os_form' : OutstationForm(),
            'car_form' : CarForm(),
            'pi_form' : PersionInfoForm(),
            'l_form' : LocalForm(),
            'ap_form' : AirPortForm(),
            'car_data' : car_data,
            'companies' : companies
        }
        
        return render(request, 'index.html', context)

@login_required
def Profile_view(request):
    p_data = request.user.profile 
    if request.method == "POST":
        user_form1 = UserForm(data=request.POST, instance=request.user)
        profile_form1 = ProfileForm(request.POST, request.FILES, instance=p_data)
        print(profile_form1)
        print(user_form1)
        if user_form1.is_valid() and profile_form1.is_valid():
            user_form1.save()
            profile_form1.save()
            messages.success(request, 'Your Profile changed Successfully', extra_tags='green')
            return redirect('/profile')
        else:
            messages.error(request, 'Somthing went Wrong!', extra_tags='red')
            return redirect('/')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=p_data)
        return render(request, 'profile.html', {"profile_form":profile_form, "user_form":user_form})


@login_required
@User_only
def Oustation_view(request):
    os_data = OutStation.objects.filter(os_user=request.user.id)
        
    return render(request, 'outstation.html', {"os_data":os_data, 'name':request.user.username})

@login_required
@User_only
def Local_view(request):
    l_data = Local.objects.filter(l_user=request.user.id)
        
    return render(request, 'local.html', {"l_data":l_data, 'name':request.user.username})

@login_required
@User_only
def Airport_view(request):
    ap_data = AirPort.objects.filter(ap_user=request.user.id)
        
    return render(request, 'airport.html', {"ap_data":ap_data, 'name':request.user.username})

@login_required
@User_only
def Live_Bookings(request):
    live_os = OutStation.objects.filter(os_user=request.user.id, os_pickup__gte=timezone.now())
    live_l = Local.objects.filter(l_user=request.user.id, l_pickup__gte=timezone.now())
    live_ap = AirPort.objects.filter(ap_user=request.user.id, ap_pickup__gte=timezone.now())

    context = {
        'live_os' : live_os,
        'live_l' : live_l,
        'live_ap' : live_ap,
        'name':request.user.username
    }
    return render(request, 'liveBook.html', context)


@login_required
@User_only
def Cancel_Booking(request, c_id):
    os_data = OutStation.objects.filter(os_persional_info=c_id)
    l_data = Local.objects.filter(l_persional_info=c_id)
    ap_data = AirPort.objects.filter(ap_persional_info=c_id)

    if bool(os_data):
        os_data.delete()
    elif bool(l_data):
        l_data.delete()
    else:
        ap_data.delete()
    messages.success(request, 'Your Booking Cancelled Successfully', extra_tags='green')   
    return redirect('/upcoming')

@login_required
@User_only
def Edit_Booking(request, c_id):
    os_data = OutStation.objects.get(pk=c_id)
    print("id if edit", c_id)
    print("khbfsbkff", os_data)
    if request.method == 'POST':        
        os_edit_form = OutstationForm(request.POST, instance=os_data)
        if os_edit_form.is_valid():
            os_edit_form.save()
            messages.success(request, 'Yor Trip Edited successfully', extra_tags='green')            
    else:
        os_edit_form = OutstationForm(instance=os_data)
        return render(request, 'liveBook.html', {'edit_form':os_edit_form, 'name':request.user.username})


def initiate_payment(request):
    if request.method == "GET":
        return render(request, 'payments/pay.html')
    try:
        username = request.POST['username']
        password = request.POST['password']
        amount = int(request.POST['amount'])
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise ValueError
        auth_login(request=request, user=user)
    except:
        return render(request, 'payments/pay.html', context={'error': 'Wrong Accound Details or amount'})

    transaction = Transaction.objects.create(made_by=user, amount=20000)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        #('MOBILE_N0', '9666146101'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'payments/redirect.html', context=paytm_params)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        paytm_checksum = ''
        print(request.body)
        print(request.POST)
        received_data = dict(request.POST)
        print(received_data)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            print("Checksum Matched")
            received_data['message'] = "Checksum Matched"
        else:
            print("Checksum Mismatched")
            received_data['message'] = "Checksum Mismatched"

        return render(request, 'payments/callback.html', context=received_data)

# def Check_date(request, from_date=None, to_date=None):
    if request.method == "GET":
        f_date = request.GET.get("from_date")
        t_date = request.GET.get("to_date")
        outStation_pickup = OutStation.objects.filter(os_pickup__gte=timezone.now()).order_by("os_pickup")
        outStation_return = OutStation.objects.filter(os_return__gte=timezone.now()).order_by("os_return")
        print(outStation_pickup, outStation_return)
        # local_dates = Local.objects.filter(l_return__lte=timezone.now())
        # airport_dates = AirPort.objects.filter(ap_return__lte=timezone.now())
        r_dates = list()
        p_dates = list()
        for x in outStation_pickup:
            xy = x.os_pickup
            p_dates.append("{}-{}-{}".format(xy.year, xy.month, xy.day))
        for y in outStation_return:
            yx = y.os_return
            r_dates.append("{}-{}-{}".format(yx.year, yx.month, yx.day))
        # for x in local_dates:
        #     xy = x.l_return
        #     dates.add("{}-{}-{}".format(xy.year, xy.month, xy.day))
        # for x in airport_dates:
        #     xy = x.ap_return
        #     dates.add("{}-{}-{}".format(xy.year, xy.month, xy.day))

        # return_dates = list(r_dates)
        # pickup_dates = list(p_dates)
        print(p_dates, r_dates)
        # date_from =  OutStation.objects.filter(os_pickup=from_date).exists()
        # print(date_from)
        # date_to =  OutStation.objects.filter(os_return= to_date).exists()
        # print(date_to)
        # if date_from  and date_to:
        # for x in return_dates:
        #     print(x)
        #     if from_date > x and to_date > x:
        #         meg = "u can book"
        #     else:
        #         meg = "u can't book"
        # for start, end in zip(p_dates, r_dates):
        #     print(start,"start")
        #     print(end,"end")
        #     print(f_date, t_date)
        #     #if  (start>f_date and end<t_date) or (start<f_date and end>t_date)  or (start<t_date and end>t_date) or (start<f_date and end>f_date):
        #     if (f_date>=start and f_date<=end) and (t_date>=start and t_date<=end):
        #         print("in")
        #         print("##############################")               
        #         break   
import datetime
@login_required
@User_only
def Check_date(request):
    if request.method == "GET":
        f_date = request.GET.get("from_date")
        t_date = request.GET.get("to_date")
        car_id = request.GET.get("c_id")
        print(car_id)
        start = datetime.datetime.strptime(f_date, '%Y-%m-%d')
        end = datetime.datetime.strptime(t_date, '%Y-%m-%d') 
        o = OutStation.objects.values('os_car').filter(Q(Q(os_pickup__gte=timezone.now()) & Q(os_car_id__c_car_id=car_id)) & Q(Q(Q(os_return__gte=start) & Q(os_return__lte=end)) | Q(Q(os_pickup__lte=end) & Q(os_pickup__gte=start)) | Q(Q(os_pickup__lte=end) & Q(os_return__gte=end)) | Q(Q(os_pickup__lte=start) & Q(os_return__gte=start))))
        l = Local.objects.values('l_car').filter(Q(Q(l_pickup__gte=timezone.now()) & Q(l_car_id__c_car_id=car_id)) & Q(Q(Q(l_return__gte=start) & Q(l_return__lte=end)) | Q(Q(l_pickup__lte=end) & Q(l_pickup__gte=start)) | Q(Q(l_pickup__lte=end) & Q(l_return__gte=end)) | Q(Q(l_pickup__lte=start) & Q(l_return__gte=start))))
        ap = AirPort.objects.values('ap_car').filter(Q(Q(ap_pickup__gte=timezone.now()) & Q(ap_car_id__c_car_id=car_id)) & Q(Q(Q(ap_return__gte=start) & Q(ap_return__lte=end)) | Q(Q(ap_pickup__lte=end) & Q(ap_pickup__gte=start)) | Q(Q(ap_pickup__lte=end) & Q(ap_return__gte=end)) | Q(Q(ap_pickup__lte=start) & Q(ap_return__gte=start))))
        
        print(o, l, ap)
        if car_id == '3':
            result = '1'
            return HttpResponse(result)
        elif car_id == '2':
            result = '1'
            return HttpResponse(result)
        result = o.count()+l.count()+ap.count()
        print(result)
        return HttpResponse(result)

@login_required
@User_only
def Autocomplete(request):
    city = City.objects.values('city_name')
    l = list()
    for x in city:
        l.append(x['city_name'])
    return HttpResponse(l)

# def Autocomplete_airport(request):
#     city = Citys.objects.values('airport_name')
#     l = list()
#     for x in city:
#         l.append(x['airport_name']+'..')
#     print(l)
#     return HttpResponse(l)
@login_required
@User_only
def Autocomplete_airport(request):
    if 'term' in request.GET:
        city = Citys.objects.filter(airport_name__icontains=request.GET.get("term"))
        l = list()
        for x in city:
            l.append(x.airport_name)
        return JsonResponse(l, safe=False)


###################    to Store CSV file data in database   ##################################

 # with open("/home/grktechnologies/myfolder/thierd_project/airport.csv") as f:
    #     import csv
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print(row)
    #         created = Citys.objects.get_or_create(airport_name=row)
    #         created.save()

@Admin_only
def AdminLiveBook(request):
    outStation_count = OutStation.objects.filter(os_pickup__gte=timezone.now()).count()
    local_count = Local.objects.filter(l_pickup__gte=timezone.now()).count()
    airport_count = AirPort.objects.filter(ap_pickup__gte=timezone.now()).count()

    context = {
        "outStation_count":outStation_count,
        "local_count":local_count,
        "airport_count":airport_count,
        "total_count": outStation_count+local_count+airport_count
    }

    return render(request, 'admin_live_booking.html', context)

@Admin_only
def AdminPreBook(request):
    outStation_count = OutStation.objects.filter(os_pickup__lt=timezone.now()).count()
    local_count = Local.objects.filter(l_pickup__lt=timezone.now()).count()
    airport_count = AirPort.objects.filter(ap_pickup__lt=timezone.now()).count()

    context = {
        "outStation_count":outStation_count,
        "local_count":local_count,
        "airport_count":airport_count,
        "total_count": outStation_count+local_count+airport_count
    }

    return render(request, 'admin_pre_booking.html', context)

    # def AdminPre_outBook(request):
    # outStation_count = OutStation.objects.filter(os_pickup__lt=timezone.now())
    # local_count = Local.objects.filter(l_pickup__lt=timezone.now())
    # airport_count = AirPort.objects.filter(ap_pickup__lt=timezone.now())

    # context = {
    #     "outStation_count":outStation_count,
    #     "local_count":local_count,
    #     "airport_count":airport_count,
    #     "total_count": outStation_count+local_count+airport_count
    # }

    # return render(request, 'admin_live_booking.html', context)

@Admin_only
def Addcar(request):
    if request.method=='POST':
        carform = CardemoForm(request.POST, request.FILES)
        if carform.is_valid():
            carform.save()
            return redirect('car_detail')
    carform = CardemoForm()
    context = {
        "carform":carform,
    }
    return render(request, 'addcar.html', context)

@Admin_only
def Cardetail(request):
    form = Cardemo.objects.all()
    return render(request, 'car_details.html', {"form":form})

@Admin_only
def Editcar(request, c_id):
    edit_car = Cardemo.objects.get(id=c_id)
    if request.method=='POST':
        form = CardemoForm(request.POST, request.FILES, instance=edit_car)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member edited successfully', extra_tags='green')
            return redirect('car_detail')
    form = CardemoForm(instance=edit_car)
    return render(request, 'edit_car.html', {"form":form})

@Admin_only
def Deletecar(request, c_id):
    delete_car = Cardemo.objects.get(id=c_id)
    delete_car.delete()
    return redirect('car_detail')

@Admin_only
def Add_Cities(request):
    form = CityForm()
    if request.method=='POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'City added successfully', extra_tags='green')
            return redirect('/')
        else:
            messages.error(request, 'City not added', extra_tags='red')
            return redirect('add_city')

    return render(request, 'add_city.html', {"form":form})


@login_required
@Admin_only
def Oustation_live_view(request):
    out_live_view = OutStation.objects.filter(os_pickup__gte=timezone.now())
        
    return render(request, 'live_view_list/outstationlive.html', {"os_data":out_live_view, 'name':request.user.username})

@login_required
@Admin_only
def Local_live_view(request):
    local_live_view = Local.objects.filter(l_pickup__gte=timezone.now())
        
    return render(request, 'live_view_list/locallive.html', {"l_data":local_live_view, 'name':request.user.username})

@login_required
@Admin_only
def Airport_live_view(request):
    ap_live_view = AirPort.objects.filter(ap_pickup__gte=timezone.now())
        
    return render(request, 'live_view_list/airportlive.html', {"ap_data":ap_live_view, 'name':request.user.username})

@login_required
@Admin_only
def Oustation_pre_view(request): 
    out_pre_view = OutStation.objects.filter(os_pickup__lt=timezone.now())
        
    return render(request, 'live_view_list/outstationpre.html', {"os_data":out_pre_view, 'name':request.user.username})

@login_required
@Admin_only
def Local_pre_view(request):
    local_pre_view = Local.objects.filter(l_pickup__lt=timezone.now())
        
    return render(request, 'live_view_list/localpre.html', {"l_data":local_pre_view, 'name':request.user.username})

@login_required
@Admin_only
def Airport_pre_view(request):
    ap_pre_view = AirPort.objects.filter(ap_pickup__lt=timezone.now())
        
    return render(request, 'live_view_list/airportpre.html', {"ap_data":ap_pre_view, 'name':request.user.username})


