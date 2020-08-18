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


# Create your views here.

def base_layout(request):
	template='base.html'
	return render(request,template)

def is_admin(request):
    return True if request.user.is_active else False

def is_superuser(request):
    return True if request.user.is_superuser else False

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username__iexact=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/home')
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('cust/login/')



def register(request):
    if request.method == "POST":
        signup = Cust_SignUpForm(request.POST)
        if signup.is_valid():
            signup.save()
            return redirect('/home')
    signup = Cust_SignUpForm()
    return render(request, 'register.html', {'signup': signup})

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
    if not is_admin(request):
        messages.error(request, 'Your Password or Username is incorrect', extra_tags='red')
        return HttpResponseRedirect('cust_login')
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

                text_message = ('Dear ' + pi_data['p_name'] +',\nThank You for Booking With KNG Travels. \nYour ID: '+ pi.p_order_id + ' You booked a '+ str(car_data['c_car']) +' '+ car_data['c_ac_type'] + ' for ' + os_data['os_from'] + ' to ' + os_data['os_to'] + ' on '+ str(os_data['os_pickup']) +' at '+ str(os_data['os_picktime'])+'. \nWe wish you a very happy and safe Journey, \nIf you have any query contact on 9666817780.')

                payload1 = {"sender_id":"FSTSMS",
                    "message":text_message,
                    "language":"english",
                    "route":'p',
                    "numbers": pi_data['p_Phone'],
                    }
                text_sms = ('Dear Nithish, \nYour '+ str(car_data['c_car'])+ ' '+ car_data['c_ac_type'] +' Booked for ' + os_data['os_from'] + ' to ' + os_data['os_to'] + ' on '+ str(os_data['os_pickup']) +' at '+ str(os_data['os_picktime'])+'. \nHis Name : ' + pi_data['p_name'] +' Contact No : ' + pi_data['p_Phone'] + ' and Mail id : ' + pi_data['p_email'] + '.')

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

                #response = requests.request("POST", url, data=payload1, headers=headers)
                #response = requests.request("POST", url, data=payload2, headers=headers)

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
                
        elif l_form.data["l_from"]:
            if l_form.is_valid() and car_form.is_valid() and pi_form.is_valid():

                
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
                message2 = ('New Booking', 'Dear Nithish, \nYour '+ str(car_data['c_car'])+ ' '+ car_data['c_ac_type'] + ' Booked for ' + l_data['l_from'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \nHis Name : ' + pi_data['p_name']+ ' Contact No : ' + pi_data['p_Phone'] + ' and Mail id ' + pi_data['p_email'] + '.', settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER,])
                send_mass_mail((message1, message2), fail_silently=False)

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
                message1 = ('New Booking', 'Dear ' + pi_data['p_name'] +',\nThank You for Booking With KNG Travles. \nYour ID: '+  pi.p_order_id + ' You booked a '+ str(car_data['c_car']) + ' '+ car_data['c_ac_type']+ ' for ' + ap_data['ap_from'] + ' to ' + ap_data['ap_to'] + ', on '+ str(ap_data['ap_pickup']) +' at '+ str(ap_data['ap_picktime'])+'. \nWe wish you a very happy and safe Journey, \nIf you have any query contact on 9666817780 .' , settings.EMAIL_HOST_USER, [pi_data['p_email'],])
                message2 = ('New Booking', 'Dear Nithish, \nYour '+ str(car_data['c_car']) + ' '+ car_data['c_ac_type']+ ' Booked for ' + ap_data['ap_city'] + ' on '+ str(ap_data['ap_pickup']) +' at '+ str(ap_data['ap_picktime'])+'. \nHis Name : ' + pi_data['p_name']+' Contact No : ' + pi_data['p_Phone'] + ', and Mail id ' + pi_data['p_email'] + '.', settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER,])
                send_mass_mail((message1, message2), fail_silently=False)

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
                return redirect('/home')
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
    if not is_admin(request):
        return HttpResponseRedirect('cust_login')
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
def Oustation_view(request):
    if not is_admin(request):
        return HttpResponseRedirect('cust_login')
    else:
        os_data = OutStation.objects.filter(os_user=request.user.id)
        
    return render(request, 'outstation.html', {"os_data":os_data, 'name':request.user.username})

@login_required
def Cancel_Booking(request, c_id):
    if not is_admin(request):
        return HttpResponseRedirect('cust_login')
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
def Edit_Booking(request, c_id):
    if not is_admin(request):
        return HttpResponseRedirect('cust_login')
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

@login_required
def Local_view(request):
    if not is_admin(request):
        return HttpResponseRedirect('cust_login')
    else :
        l_data = Local.objects.filter(l_user=request.user.id)
        
    return render(request, 'local.html', {"l_data":l_data, 'name':request.user.username})

@login_required
def Airport_view(request):
    if not is_admin(request):
        return HttpResponseRedirect('cust_login')
    else :
        ap_data = AirPort.objects.filter(ap_user=request.user.id)
        
    return render(request, 'airport.html', {"ap_data":ap_data, 'name':request.user.username})

@login_required
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
        result = o.count()+l.count()+ap.count()
        print(result)
        return HttpResponse(result)


