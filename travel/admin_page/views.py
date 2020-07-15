from django.shortcuts import render, redirect , HttpResponseRedirect, reverse
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

# Create your views here.

def is_admin(request):
    return True if request.user.is_active else False

def is_superuser(request):
    return True if request.user.is_superuser else False

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('home/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('cust/login/')



def register(request):
    if request.method == "POST":
        signup = Student_SignUpForm(request.POST)
        if signup.is_valid():
            signup.save()
            return HttpResponseRedirect('/home/')
    signup = Student_SignUpForm()
    return render(request, 'register.html', {'signup': signup})

@login_required
def Outstation(request):
    if not is_admin(request):
        messages.error(request, 'Your Password or Username is incorrect', extra_tags='red')
        return HttpResponseRedirect('cust_login')
    if request.method == "POST":
        amount = int(request.POST['amount'])
        os_form = OutstationForm(request.POST )
        l_form= LocalForm(request.POST)
        ap_form = AirPortForm(request.POST)
        car_form = CarForm(request.POST)
        pi_form = PersionInfoForm(request.POST)
        if os_form.data["os_from"]:
            if os_form.is_valid() and car_form.is_valid() and pi_form.is_valid():

                os_data = os_form.cleaned_data
                os = os_form.save(commit=False)
                os.os_user = request.user
                os.save()

                car = car_form.cleaned_data.get("c_car")
                cr = car_form.save(commit=False)
                cr.c_user = request.user
                cr.save()
                
                name = pi_form.cleaned_data.get("p_name")
                mail = pi_form.cleaned_data.get("p_emai")
                contact = pi_form.cleaned_data.get("p_Phone")
                pi = pi_form.save(commit=False)
                pi.p_user = request.user
                pi.save()

                ############### payment gateway ####################

                
      
                #return render(request, 'payments/pay.html', context={'error': 'Wrong Accound Details or amount'})

                transaction = Transaction.objects.create(made_by=request.user, amount=amount)
                transaction.save()
                merchant_key = settings.PAYTM_SECRET_KEY

                params = (
                    ('MID', settings.PAYTM_MERCHANT_ID),
                    ('ORDER_ID', str(transaction.order_id)),
                    ('CUST_ID', str(transaction.made_by.email)),
                    ('TXN_AMOUNT', str(transaction.amount)),
                    ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
                    ('WEBSITE', settings.PAYTM_WEBSITE),
                    ('EMAIL', mail),
                    ('MOBILE_N0', contact),
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

                message1 = ('New Booking', 'Dear ' + name +',\n Thank for Booking With KNG Travles. \n You booked a '+ str(car) + ' for ' + os_data['os_from'] + ' on '+ str(os_data['os_pickup']) +' at '+ str(os_data['os_picktime'])+'. \n We wish you a very happy and safe Journey, \n if you have any query contact on 9666817780 .' , 'itsmak100@gmail.com', [mail,])
                message2 = ('New Booking', 'Dear ' + name +',\n Booked a '+ str(car) + ' for ' + os_data['os_from'] + ' on '+ str(os_data['os_pickup']) +' at '+ str(os_data['os_picktime'])+'. \n his Contact No : ' + contact + ' and Mail id ' + mail + '.', 'itsmak100@gmail.com', [mail,])
                send_mass_mail((message1, message2), fail_silently=False)

                return render(request, 'payments/redirect.html', context=paytm_params)
                
        elif l_form.data["l_city"]:
            if l_form.is_valid() and car_form.is_valid() and pi_form.is_valid():

                l_data = l_form.cleaned_data
                l = l_form.save(commit=False)
                l.l_user = request.user
                l.save()
                
                car = car_form.cleaned_data.get("c_car")
                cr = car_form.save(commit=False)
                cr.c_user = request.user
                cr.save() 

                name = pi_form.cleaned_data.get("p_name")
                mail = pi_form.cleaned_data.get("p_emai")
                contact = pi_form.cleaned_data.get("p_Phone")
                pi = pi_form.save(commit=False)
                pi.p_user = request.user
                pi.save()

                context = {
                    'name' : name,
                    'car' : car,
                    'l_data' : l_data,
                }
                ########### to send multiple sms's  ###############

                # message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
                # message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
                # send_mass_mail((message1, message2), fail_silently=False)
                message1 = ('New Booking', 'Dear ' + name +',\n Thank for Booking With KNG Travles. \n You booked a '+ str(car) + ' for ' + l_data['l_city'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \n We wish you a very happy and safe Journey, \n if you have any query contact on 9666817780 .' , 'itsmak100@gmail.com', [mail,])
                message2 = ('New Booking', 'Dear ' + name +',\n Booked a '+ str(car) + ' for ' + l_data['l_city'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \n his Contact No : ' + contact + ' and Mail id ' + mail + '.', 'itsmak100@gmail.com', [mail,])
                send_mass_mail((message1, message2), fail_silently=False)
                #send_mail('New Booking', 'Dear ' + name +',\n'+ 'Thank for Booking With KNG Travles. \n You booked '+ car + ' for ' + l_data['l_city'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \n We wish you a very happy and safe Journey, \n if you have any query contact on 9666817780 .' , 'itsmak100@gmail.com', [mail,], fail_silently=False)
                return render(request, 'thankq.html', context)
            
        elif ap_form.data["ap_city"]:
            if ap_form.is_valid() and car_form.is_valid() and pi_form.is_valid():

                ap_data = ap_form.cleaned_data                
                ap = ap_form.save(commit=False)
                ap.save()


                car = car_form.cleaned_data.get("c_car")
                cr = car_form.save(commit=False)
                cr.cr_user = request.user.username
                cr.save() 

                name = pi_form.cleaned_data.get("p_name")
                mail = pi_form.cleaned_data.get("p_emai")
                contact = pi_form.cleaned_data.get("p_Phone")
                pi = pi_form.save(commit=False)
                pi.p_user = request.user.username
                pi.save()

                context = {
                    'name' : name,
                    'car' : car,
                    'ap_data' : ap_data,
                }

                ########### to send multiple sms's  ###############

                # message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
                # message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
                # send_mass_mail((message1, message2), fail_silently=False)
                message1 = ('New Booking', 'Dear ' + name +',\n Thank for Booking With KNG Travles. \n You booked a '+ car + ' for ' + l_data['l_city'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \n We wish you a very happy and safe Journey, \n if you have any query contact on 9666817780 .' , 'itsmak100@gmail.com', [mail,])
                message2 = ('New Booking', 'Dear ' + name +',\n Booked a '+ car + ' for ' + l_data['l_city'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \n his Contact No : ' + contact + ' and Mail id ' + mail + '.', 'itsmak100@gmail.com', [mail,])
                send_mass_mail((message1, message2), fail_silently=False)
                #send_mail('New Booking', 'Dear ' + name +',\n'+ 'Thank for Booking With KNG Travles. \n You booked '+ car + ' for ' + l_data['l_city'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \n We wish you a very happy and safe Journey, \n if you have any query contact on 9666817780 .' , 'itsmak100@gmail.com', [mail,], fail_silently=False)
                return render(request, 'thankq.html', context)
        
   
        
                   
            else:
                messages.error(request, 'Somthing went Wrong!', extra_tags='red')
                return redirect('home')
    else:
        context = {
            'os_form' : OutstationForm(),
            'car_form' : CarForm(),
            'pi_form' : PersionInfoForm(),
            'l_form' : LocalForm(),
            'ap_form' : AirPortForm()
        }
        
        return render(request, 'outstation.html', context)





def demo(request):
    return render(request, 'thankq.html')



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
