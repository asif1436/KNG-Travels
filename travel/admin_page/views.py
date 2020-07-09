from django.shortcuts import render, redirect , HttpResponseRedirect
from admin_page.models import *
from admin_page.forms import *
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail


# Create your views here.


def Outstation(request):
    if request.method == "POST":
        os_form = OutstationForm(request.POST )
        l_form= LocalForm(request.POST)
        ap_form = AirPortForm(request.POST)
        car_form = CarForm(request.POST)
        pi_form = PersionInfoForm(request.POST)
        if os_form.data["os_trip_type"]:
            if os_form.is_valid() and car_form.is_valid() and pi_form.is_valid():

                os_data = os_form.cleaned_data
                os = os_form.save(commit=False)
                os.save()

                car = car_form.cleaned_data.get("c_car")
                cr = car_form.save(commit=False)
                cr.c_os = os
                cr.save()
                
                name = pi_form.cleaned_data.get("p_name")
                pi = pi_form.save(commit=False)
                pi.p_os = os
                pi.save()

                context = {
                    'name' : name,
                    'car' : car,
                    'os_data' : os_data,
                }

                return render(request, 'thankq.html', context)
            
        elif l_form.data["l_city"]:
            if l_form.is_valid() and car_form.is_valid() and pi_form.is_valid():

                l_data = l_form.cleaned_data
                l = l_form.save(commit=False)
                l.save()
                
                car = car_form.cleaned_data.get("c_car")
                cr = car_form.save(commit=False)
                cr.c_local = l
                cr.save() 

                name = pi_form.cleaned_data.get("p_name")
                mail = pi_form.cleaned_data.get("p_emai")
                contact = pi_form.cleaned_data.get("p_Phone")
                pi = pi_form.save(commit=False)
                pi.p_local = l
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
                message1 = ('New Booking', 'Dear ' + name +',\n Thank for Booking With KNG Travles. \n You booked a '+ car + ' for ' + l_data['l_city'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \n We wish you a very happy and safe Journey, \n if you have any query contact on 9666817780 .' , 'itsmak100@gmail.com', [mail,])
                message2 = ('New Booking', 'Dear ' + name +',\n Booked a '+ car + ' for ' + l_data['l_city'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \n his Contact No : ' + contact + ' and Mail id ' + mail + '.', 'itsmak100@gmail.com', [mail,])
                send_mass_mail((message1, message2), fail_silently=False)
                #send_mail('New Booking', 'Dear ' + name +',\n'+ 'Thank for Booking With KNG Travles. \n You booked '+ car + ' for ' + l_data['l_city'] + ' on '+ str(l_data['l_pickup']) +' at '+ str(l_data['l_picktime'])+'. \n We wish you a very happy and safe Journey, \n if you have any query contact on 9666817780 .' , 'itsmak100@gmail.com', [mail,], fail_silently=False)
                return render(request, 'thankq.html', context)
            
        elif ap_form.data["ap_city"]:
            if ap_form.is_valid() and car_form.is_valid() and pi_form.is_valid():

                ap_data = ap_form.cleaned_data                
                ap = ap_form.save(commit=False)
                ap.save()


                car = car_form.cleaned_data.get("c_car")
                print(car)
                cr = car_form.save(commit=False)
                cr.c_ap = ap
                cr.save() 

                name = pi_form.cleaned_data.get("p_name")
                print(name)
                pi = pi_form.save(commit=False)
                pi.p_ap = ap
                pi.save()

                context = {
                    'name' : name,
                    'car' : car,
                    'ap_data' : ap_data,
                }

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