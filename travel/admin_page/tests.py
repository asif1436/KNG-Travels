#from django.test import TestCase
# import numpy as np
import pandas as pd
# from django.shortcuts import render, redirect , HttpResponseRedirect, reverse, HttpResponse
# from admin_page.models import *
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
# from django.core import serializers
# import numpy as np
# from django.utils import timezone
# # Create your tests here.

# date1 = ['2020-08-01', '2020-08-15', '2020-08-19']
# date2 = ['2020-08-02', '2020-08-17', '2020-08-20']

# f_date = '2020-08-07'
# t_date = '2020-08-16'
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
ab = '''Ada, Telangana, India..Adegaon, Telangana, India..Adilabad, Telangana, India..Adilabad Collectorate, Telangana, India..Agm Colony, Telangana, India..Ainam, Telangana, India..Aknepalli, Telangana, India..Akoli, Telangana, India..Alegaon, Telangana, India..Aloor, Telangana, India..Ambaripet, Telangana, India..Andavelli, Telangana, India..Andugulpet, Telangana, India..Andukur, Telangana, India..Angarajpally, Telangana, India..Ankhoda, Telangana, India..Ankoli, Telangana, India..Annaram, Telangana, India..Arepally, Telangana, India..Arli (T), Telangana, India..Ashepally, Telangana, India..Ashta, Telangana, India..Asifabad, Telangana, India..Asnad, Telangana, India..Awadam, Telangana, India..Babapur, Telangana, India..Babasagar, Telangana, India..Badampally, Telangana, India..Badankurthy, Telangana, India..Bambara, Telangana, India..Bangalpet, Telangana, India..Bansapalli, Telangana, India..Bapur, Telangana, India..Bareguda, Telangana, India..Basar  (Adilabad), Telangana, India..Bazar Hathnur, Telangana, India..Beernandi, Telangana, India..Bejjur, Telangana, India..Bela, Telangana, India..Bellalbadi, Telangana, India..Bellampalli, Telangana, India..Bellampalli R.S., Telangana, India..Beltharoda, Telangana, India..Bhagyanagar  (Adilabad), Telangana, India..Bhainsa  (Adilabad), Telangana, India..Bharampur, Telangana, India..Bheemaram, Telangana, India..Bheempur, Telangana, India..Bheemsari, Telangana, India..Bhimini, Telangana, India..Bholsa, Telangana, India..Bhosi, Telangana, India..Bhuktapur, Telangana, India..Bhutai, Telangana, India..Bibra, Telangana, India..Bidrelli, Telangana, India..Birsaipet, Telangana, India..Birvelli, Telangana, India..Boath, Telangana, India..Bodepalli, Telangana, India..Boregaon, Telangana, India..Boregaon, Telangana, India..Borigaon, Telangana, India..Boyapalli, Telangana, India..Brahmangaon, Telangana, India..Budakalan, Telangana, India..Budakurd, Telangana, India..Buggaram, Telangana, India..Burguda, Telangana, India..Chakepalli, Telangana, India..Chanda (T), Telangana, India..Chandaram, Telangana, India..Chandur, Telangana, India..Chaprala, Telangana, India..Chata, Telangana, India..Chedwai, Telangana, India..Chichdhari Khanapur, Telangana, India..Chichondi, Telangana, India..Chincholi (B), Telangana, India..Chinchughat, Telangana, India..Chinnoor, Telangana, India..Chintaguda, Telangana, India..Chintaguda, Telangana, India..Chintakunta, Telangana, India..Chintalamanepalli, Telangana, India..Chintalbori, Telangana, India..Chintalchanda, Telangana, India..Chirrakunta, Telangana, India..Chityal, Telangana, India..Chityal, Telangana, India..Chondi, Telangana, India..Chorpalli, Telangana, India..Coal Chemical Complex, Telangana, India..Cotton Market, Telangana, India..Dabba, Telangana, India..Dandepalli, Telangana, India..Dantanpalli, Telangana, India..Dasnapur, Telangana, India..Dasnapur Colony, Telangana, India..Dasnapur Colony  D., Telangana, India..Dasturabad, Telangana, India..Deepaiguda, Telangana, India..Dehgaon, Telangana, India..Dehgaon, Telangana, India..Dehgaon, Telangana, India..Devaiguda, Telangana, India..Devapur, Telangana, India..Devapur, Telangana, India..Devapur Cement Works, Telangana, India..Dewalwada, Telangana, India..Dhaba, Telangana, India..Dhaboli, Telangana, India..Dhani, Telangana, India..Dhannoor, Telangana, India..Dhanora(B), Telangana, India..Dharmaram, Telangana, India..Dharmaraopet, Telangana, India..Dhorpalli, Telangana, India..Dilawarpur, Telangana, India..Dilawarpur, Telangana, India..Dimda, Telangana, India..Dimmadurthy, Telangana, India..Doderna, Telangana, India..Donabanda, Telangana, India..Dowdepally, Telangana, India..Dugnepally, Telangana, India..Dwaraka, Telangana, India..Dwarakapur, Telangana, India..Easgaon - V, Telangana, India..Easgaon Camp, Telangana, India..Echoda, Telangana, India..Elegaon, Telangana, India..Elvi, Telangana, India..Gadapur, Telangana, India..Gadchanda, Telangana, India..Gadiguda, Telangana, India..Gandhi Chowk  (Adilabad), Telangana, India..Gangapur, Telangana, India..Ghanpur, Telangana, India..Ghanpur, Telangana, India..Ghotkuri, Telangana, India..Ginnedhari, Telangana, India..Ginnera, Telangana, India..Girjam, Telangana, India..Girnoor, Telangana, India..Girvelli, Telangana, India..Gokonda, Telangana, India..Gollakota, Telangana, India..Golleti, Telangana, India..Gonedhanora, Telangana, India..Gopalpet, Telangana, India..Gourapur, Telangana, India..Gowliguda, Telangana, India..Goyagaon, Telangana, India..Grain Market  (Adilabad), Telangana, India..Guda, Telangana, India..Gudamamda, Telangana, India..Gudem, Telangana, India..Gudem, Telangana, India..Gudihatnoor, Telangana, India..Gudipet, Telangana, India..Gudlabori, Telangana, India..Gulmadugu, Telangana, India..Gumma  (Adilabad), Telangana, India..Gundaipet, Telangana, India..Gundampalli, Telangana, India..Gundi, Telangana, India..Gunjala, Telangana, India..Gurjal, Telangana, India..Gurjamannur, Telangana, India..Gurudpet, Telangana, India..Harkapur, Telangana, India..Harnath Colony, Telangana, India..Hasnapur, Telangana, India..Hathini, Telangana, India..Hazipur, Telangana, India..Hudkuli, Telangana, India..Indanpally, Telangana, India..Indaram, Telangana, India..Indervelli, Telangana, India..Indhani, Telangana, India..Indiranagar  (Adilabad), Telangana, India..Industrial Area  (Adilabad), Telangana, India..Itikyal, Telangana, India..Ityal, Telangana, India..Jainad, Telangana, India..Jainoor, Telangana, India..Jaipur, Telangana, India..Jajjarvelli, Telangana, India..Jam, Telangana, India..Jamni, Telangana, India..Janakapur, Telangana, India..Jandavenkatapur, Telangana, India..Jangaon, Telangana, India..Jannaram, Telangana, India..Jatharla, Telangana, India..Jawla, Telangana, India..Jhary, Telangana, India..Jilleda, Telangana, India..Kadthal, Telangana, India..Kalamadugu, Telangana, India..Kallur, Telangana, India..Kalwa, Telangana, India..Kalwada, Telangana, India..Kalyani Khani, Telangana, India..Kamalkot, Telangana, India..Kamole, Telangana, India..Kampamediguda, Telangana, India..Kanchanpalli, Telangana, India..Kanchevelli, Telangana, India..Kankapur, Telangana, India..Kannepalli, Telangana, India..Kannepalli, Telangana, India..Kannergaon, Telangana, India..Kapparla, Telangana, India..Karanji, Telangana, India..Karathwada, Telangana, India..Karjavelli, Telangana, India..Karjibheempur, Telangana, India..Karnamamidi, Telangana, India..Kasba  (Adilabad), Telangana, India..Kasipet, Telangana, India..Kerameri, Telangana, India..Keslapur, Telangana, India..Khairdatwa, Telangana, India..Khairgaon, Telangana, India..Khamana, Telangana, India..Khanapur  (Adilabad), Telangana, India..Khirdi, Telangana, India..Khodad, Telangana, India..Khogdur, Telangana, India..Kirgul, Telangana, India..Kistampet, Telangana, India..Kistapur, Telangana, India..Kistapur, Telangana, India..Kokasmannur, Telangana, India..Kolhari, Telangana, India..Kollur, Telangana, India..Kolur, Telangana, India..Kommera, Telangana, India..Kondampally, Telangana, India..Koora, Telangana, India..Koratkal, Telangana, India..Kortakal, Telangana, India..Korvichelma, Telangana, India..Kosai R.S., Telangana, India..Kotapalli, Telangana, India..Kothalgaon, Telangana, India..Kothapalli, Telangana, India..Kothmeer, Telangana, India..Koutha (B), Telangana, India..Koutla, Telangana, India..Koutla (K), Telangana, India..Kowthala, Telangana, India..Kubeer, Telangana, India..Kuchanpally, Telangana, India..Kuchlapur, Telangana, India..Kuchlapur, Telangana, India..Kumhari, Telangana, India..Kundaram, Telangana, India..Kuntala, Telangana, India..Kushnepalli, Telangana, India..Kyathanpalli, Telangana, India..Kyathanpally, Telangana, India..Lachampur, Telangana, India..Lakkaram, Telangana, India..Laxmanchanda, Telangana, India..Laxmipur, Telangana, India..Limba (K), Telangana, India..Lingapur, Telangana, India..Lingapur, Telangana, India..Lingapur, Telangana, India..Lingi, Telangana, India..Lohesra, Telangana, India..Lonavelli, Telangana, India..Luxettipet, Telangana, India..M.G. Road, Telangana, India..Madapur, Telangana, India..Madaram Township, Telangana, India..Madaripeta, Telangana, India..Maddikal, Telangana, India..Maddipadaga, Telangana, India..Mahagaon, Telangana, India..Mahagaon, Telangana, India..Mahalingi, Telangana, India..Malak Chincholi, Telangana, India..Malegoan, Telangana, India..Mallampet, Telangana, India..Mallapur, Telangana, India..Malledi, Telangana, India..Malyal, Telangana, India..Mamda, Telangana, India..Mamidighat, Telangana, India..Mamidipalli, Telangana, India..Mamidipalli, Telangana, India..Mancherial, Telangana, India..Mancherial Bazar, Telangana, India..Mancherial Cement Works, Telangana, India..Mandamarri Colleries, Telangana, India..Mandamarri R.S., Telangana, India..Mandapalli, Telangana, India..Mangi, Telangana, India..Manikyapur, Telangana, India..Manjulapur, Telangana, India..Mankapur, Telangana, India..Manmad, Telangana, India..Marlapally, Telangana, India..Marlawai, Telangana, India..Marthidi, Telangana, India..Mavala, Telangana, India..Medpalli, Telangana, India..Metpalli, Telangana, India..Metpally, Telangana, India..Mittapalli Jagir, Telangana, India..Modela, Telangana, India..Modi, Telangana, India..Mogardhagar, Telangana, India..Moindagudipet, Telangana, India..Moogavelli, Telangana, India..Mosam, Telangana, India..Movad, Telangana, India..Mudhole, Telangana, India..Mujgi, Telangana, India..Mukhra (B), Telangana, India..Mulkala, Telangana, India..Mulkalpet, Telangana, India..Mulmadugu, Telangana, India..Munial, Telangana, India..Munjampalli, Telangana, India..Muthnur, Telangana, India..Muthnur, Telangana, India..Muthyampet, Telangana, India..Mylaram, Telangana, India..Nachan Yelcapur, Telangana, India..Nagalkonda, Telangana, India..Nagapur, Telangana, India..Nagapur, Telangana, India..Nakkalapally, Telangana, India..Nambal, Telangana, India..Namnoor, Telangana, India..Nandarampally, Telangana, India..Narayanpur, Telangana, India..Narnoor, Telangana, India..Narsapur, Telangana, India..Narsapur, Telangana, India..Narsapur  (Adilabad), Telangana, India..Naseerabad, Telangana, India..Naspur, Telangana, India..Natrajnagar, Telangana, India..Navegaon, Telangana, India..Neelwai, Telangana, India..Nennel, Telangana, India..Neradigonda, Telangana, India..Netnoor, Telangana, India..New Pipri, Telangana, India..Nigwa, Telangana, India..Nirala, Telangana, India..Nirmal  (Adilabad), Telangana, India..Ola, Telangana, India..Old Town, Telangana, India..Ootnur, Telangana, India..Ootsurangapalli, Telangana, India..Pakpatla, Telangana, India..Palli (B), Telangana, India..Panchagudi, Telangana, India..Pangdi, Telangana, India..Pangidimadra, Telangana, India..Papannapet, Telangana, India..Pardi, Telangana, India..Pardi (B), Telangana, India..Pardi (K), Telangana, India..Parimandal, Telangana, India..Parpally, Telangana, India..Parpally, Telangana, India..Patha Mancherial, Telangana, India..Patha Yelcapur, Telangana, India..Patnapur, Telangana, India..Patnapur, Telangana, India..Peddampet, Telangana, India..Peddapet, Telangana, India..Peddur, Telangana, India..Peechara, Telangana, India..Pegdapally, Telangana, India..Pembi, Telangana, India..Penchikalpet, Telangana, India..Pendalwada, Telangana, India..Pendapally, Telangana, India..Perkapally, Telangana, India..Phulara, Telangana, India..Pippaldhari, Telangana, India..Pippalkoti, Telangana, India..Pipri, Telangana, India..Pipri, Telangana, India..Pochera, Telangana, India..Pochera, Telangana, India..Pokkur, Telangana, India..Police Colony, Telangana, India..Ponkal, Telangana, India..Ponkal, Telangana, India..Ponkur, Telangana, India..Ponnaram, Telangana, India..Ponnari, Telangana, India..Powna, Telangana, India..Pownur, Telangana, India..Pulimadugu, Telangana, India..Pulsi, Telangana, India..Puspur, Telangana, India..Qawal, Telangana, India..Raipally, Telangana, India..Raipur Kandli, Telangana, India..Rajura, Telangana, India..Rajura, Telangana, India..Ramai, Telangana, India..Ramakrishnapur, Telangana, India..Rampur, Telangana, India..Rampur, Telangana, India..Rasimetta, Telangana, India..Raspalli, Telangana, India..Ratnapur Kandli, Telangana, India..Rebbanapally, Telangana, India..Rebbena, Telangana, India..Rebbena, Telangana, India..Rebbena, Telangana, India..Rechini, Telangana, India..Repallewada, Telangana, India..Revojipet, Telangana, India..RGU IIIT Campus Basar, Telangana, India..Rompalli, Telangana, India..Rp Colony, Telangana, India..Ruyyadi, Telangana, India..Saidpur, Telangana, India..Salewada, Telangana, India..Sangvi, Telangana, India..Sangvi, Telangana, India..Sanjeevnagar, Telangana, India..Sarangapur, Telangana, India..Sathanapalli, Telangana, India..Sawapur, Telangana, India..Sawli, Telangana, India..Shampur, Telangana, India..Shantapur, Telangana, India..Shanthi Khani, Telangana, India..Shetpally, Telangana, India..Shettihadapnur, Telangana, India..Siddalkunta, Telangana, India..Singapur, Telangana, India..Sirchelma, Telangana, India..Sirgapur, Telangana, India..Sirkonda, Telangana, India..Sirpur (T), Telangana, India..Sirpur (U), Telangana, India..Sirpur Khagaznagar, Telangana, India..Sirsa, Telangana, India..Sirsanna, Telangana, India..Sitagondi, Telangana, India..Soan, Telangana, India..Soanpally, Telangana, India..Somagudem Coal Mines, Telangana, India..Somanpally, Telangana, India..Sonala, Telangana, India..Sonari, Telangana, India..Srirampur Colony, Telangana, India..Station Road  (Adilabad), Telangana, India..Suddal, Telangana, India..Sunkidi, Telangana, India..Sunkli, Telangana, India..Surdapur, Telangana, India..Surjapur, Telangana, India..Tadihadapnur, Telangana, India..Talamadri, Telangana, India..Talamadugu, Telangana, India..Tallapet, Telangana, India..Talodi, Telangana, India..Tamsi, Telangana, India..Tandra, Telangana, India..Tandur (A), Telangana, India..Tantoli, Telangana, India..Tanur, Telangana, India..Tapalpur, Telangana, India..Tarnam, Telangana, India..Tekumatla, Telangana, India..Tembi, Telangana, India..Thammapur, Telangana, India..Thimmapur, Telangana, India..Tiryani, Telangana, India..Tosham, Telangana, India..Toyaguda, Telangana, India..Tumpalli, Telangana, India..Tungeda, Telangana, India..Udumpur, Telangana, India..Ullipittadorli, Telangana, India..Umri, Telangana, India..Ushegaon, Telangana, India..Velagnur, Telangana, India..Vemanpally, Telangana, India..Vempalli, Telangana, India..Vempalli, Telangana, India..Vengwapet, Telangana, India..Venkatapur, Telangana, India..Venkatapur, Telangana, India..Venkatapur, Telangana, India..Venkatraopet, Telangana, India..Waddial, Telangana, India..Waddur, Telangana, India..Wadgaon, Telangana, India..Waghapur, Telangana, India..Wankidi, Telangana, India..Wankidi, Telangana, India..Wegaon, Telangana, India..Wellal, Telangana, India..Yapalguda, Telangana, India..Yedbid, Telangana, India..Yellapalli, Telangana, India..Yellaram, Telangana, India..Yellawath, Telangana, India..Yelmal, Telangana, India..Yenda, Telangana, India..'''

ab1 = ab.split('..')
print(ab1)
xyz = pd.DataFrame(ab1)
xyz.to_csv(r'city.csv', index=False, header=True)

# x = 'Ada Adegaon Adilabad  adilabadAdilabad Collectorate  agmAgm Colony Ainam Aknepalli Akoli Alegaon Aloor Ambaripet Andavelli Andugulpet Andukur Angarajpally Ankhoda Ankoli Annaram Arepally  arli-(t)Arli (T) Ashepally Ashta Asifabad Asnad Awadam Babapur Babasagar Badampally Badankurthy Bambara Bangalpet Bansapalli Bapur Bareguda  basar--(adilabad)Basar  (Adilabad) bazarBazar Hathnur Beernandi Bejjur Bela Bellalbadi Bellampalli  bellampalli-r.s.Bellampalli R.S. Beltharoda  bhagyanagar--(adilabad)Bhagyanagar  (Adilabad) bhainsa--(adilabad)Bhainsa  (Adilabad)Bharampur Bheemaram Bheempur Bheemsari Bhimini Bholsa Bhosi Bhuktapur Bhutai Bibra Bidrelli Birsaipet Birvelli Boath Bodepalli Boregaon Boregaon Borigaon Boyapalli Brahmangaon Budakalan Budakurd Buggaram Burguda Chakepalli  chanda-(t)Chanda (T) Chandaram Chandur Chaprala Chata Chedwai  chichdhariChichdhari Khanapur Chichondi  chincholi-(b)Chincholi (B) Chinchughat Chinnoor Chintaguda Chintaguda Chintakunta Chintalamanepalli Chintalbori Chintalchanda Chirrakunta Chityal Chityal Chondi Chorpalli  coal-chemicalCoal Chemical Complex  cottonCotton Market Dabba Dandepalli Dantanpalli Dasnapur  dasnapurDasnapur Colony  dasnapur-colony--d.Dasnapur Colony  D.Dasturabad Deepaiguda Dehgaon Dehgaon Dehgaon Devaiguda Devapur Devapur  devapur-cementDevapur Cement Works Dewalwada Dhaba Dhaboli Dhani Dhannoor  dhanora(b)Dhanora(B) Dharmaram Dharmaraopet Dhorpalli Dilawarpur Dilawarpur Dimda Dimmadurthy Doderna Donabanda Dowdepally Dugnepally Dwaraka Dwarakapur  easgaon---vEasgaon - V  easgaonEasgaon Camp Echoda Elegaon Elvi Gadapur Gadchanda Gadiguda  gandhi-chowk--(adilabad)Gandhi Chowk  (Adilabad)Gangapur Ghanpur Ghanpur Ghotkuri Ginnedhari Ginnera Girjam Girnoor Girvelli Gokonda Gollakota Golleti Gonedhanora Gopalpet Gourapur Gowliguda Goyagaon  grain-market--(adilabad)Grain Market  (Adilabad)Guda Gudamamda Gudem Gudem Gudihatnoor Gudipet Gudlabori Gulmadugu  gumma--(adilabad)Gumma  (Adilabad)Gundaipet Gundampalli Gundi Gunjala Gurjal Gurjamannur Gurudpet Harkapur  harnathHarnath Colony Hasnapur Hathini Hazipur Hudkuli Indanpally Indaram Indervelli Indhani  indiranagar--(adilabad)Indiranagar  (Adilabad) industrial-area--(adilabad)Industrial Area  (Adilabad)Itikyal Ityal Jainad Jainoor Jaipur Jajjarvelli Jam Jamni Janakapur Jandavenkatapur Jangaon Jannaram Jatharla Jawla Jhary Jilleda Kadthal Kalamadugu Kallur Kalwa Kalwada  kalyaniKalyani Khani Kamalkot Kamole Kampamediguda Kanchanpalli Kanchevelli Kankapur Kannepalli Kannepalli Kannergaon Kapparla Karanji Karathwada Karjavelli Karjibheempur Karnamamidi  kasba--(adilabad)Kasba  (Adilabad)Kasipet Kerameri Keslapur Khairdatwa Khairgaon Khamana  khanapur--(adilabad)Khanapur  (Adilabad)Khirdi Khodad Khogdur Kirgul Kistampet Kistapur Kistapur Kokasmannur Kolhari Kollur Kolur Kommera Kondampally Koora Koratkal Kortakal Korvichelma  kosai-r.s.Kosai R.S. Kotapalli Kothalgaon Kothapalli Kothmeer  koutha-(b)Koutha (B) Koutla  koutla-(k)Koutla (K) Kowthala Kubeer Kuchanpally Kuchlapur Kuchlapur Kumhari Kundaram Kuntala Kushnepalli Kyathanpalli Kyathanpally Lachampur Lakkaram Laxmanchanda Laxmipur  limba-(k)Limba (K) Lingapur Lingapur Lingapur Lingi Lohesra Lonavelli Luxettipet  m.g.M.G. Road Madapur  madaramMadaram Township Madaripeta Maddikal Maddipadaga Mahagaon Mahagaon Mahalingi  malakMalak Chincholi Malegoan Mallampet Mallapur Malledi Malyal Mamda Mamidighat Mamidipalli Mamidipalli Mancherial  mancherialMancherial Bazar  mancherial-cementMancherial Cement Works  mandamarriMandamarri Colleries  mandamarri-r.s.Mandamarri R.S. Mandapalli Mangi Manikyapur Manjulapur Mankapur Manmad Marlapally Marlawai Marthidi Mavala Medpalli Metpalli Metpally  mittapalliMittapalli Jagir Modela Modi Mogardhagar Moindagudipet Moogavelli Mosam Movad Mudhole Mujgi  mukhra-(b)Mukhra (B) Mulkala Mulkalpet Mulmadugu Munial Munjampalli Muthnur Muthnur Muthyampet Mylaram  nachanNachan Yelcapur Nagalkonda Nagapur Nagapur Nakkalapally Nambal Namnoor Nandarampally Narayanpur Narnoor Narsapur Narsapur  narsapur--(adilabad)Narsapur  (Adilabad)Naseerabad Naspur Natrajnagar Navegaon Neelwai Nennel Neradigonda Netnoor  newNew Pipri Nigwa Nirala  nirmal--(adilabad)Nirmal  (Adilabad)Ola  oldOld Town Ootnur Ootsurangapalli Pakpatla  palli-(b)Palli (B) Panchagudi Pangdi Pangidimadra Papannapet Pardi  pardi-(b)Pardi (B)  pardi-(k)Pardi (K) Parimandal Parpally Parpally  pathaPatha Mancherial  pathaPatha Yelcapur Patnapur Patnapur Peddampet Peddapet Peddur Peechara Pegdapally Pembi Penchikalpet Pendalwada Pendapally Perkapally Phulara Pippaldhari Pippalkoti Pipri Pipri Pochera Pochera Pokkur  policePolice Colony Ponkal Ponkal Ponkur Ponnaram Ponnari Powna Pownur Pulimadugu Pulsi Puspur Qawal Raipally  raipurRaipur Kandli Rajura Rajura Ramai Ramakrishnapur Rampur Rampur Rasimetta Raspalli  ratnapurRatnapur Kandli Rebbanapally Rebbena Rebbena Rebbena Rechini Repallewada Revojipet  rgu-iiit-campusRGU IIIT Campus Basar Rompalli  rpRp Colony Ruyyadi Saidpur Salewada Sangvi Sangvi Sanjeevnagar Sarangapur Sathanapalli Sawapur Sawli Shampur Shantapur  shanthiShanthi Khani Shetpally Shettihadapnur Siddalkunta Singapur Sirchelma Sirgapur Sirkonda  sirpur-(t)Sirpur (T)  sirpur-(u)Sirpur (U)  sirpurSirpur Khagaznagar Sirsa Sirsanna Sitagondi Soan Soanpally  somagudem-coalSomagudem Coal Mines Somanpally Sonala Sonari  srirampurSrirampur Colony  station-road--(adilabad)Station Road  (Adilabad)Suddal Sunkidi Sunkli Surdapur Surjapur Tadihadapnur Talamadri Talamadugu Tallapet Talodi Tamsi Tandra  tandur-(a)Tandur (A) Tantoli Tanur Tapalpur Tarnam Tekumatla Tembi Thammapur Thimmapur Tiryani Tosham Toyaguda Tumpalli Tungeda Udumpur Ullipittadorli Umri Ushegaon Velagnur Vemanpally Vempalli Vempalli Vengwapet Venkatapur Venkatapur Venkatapur Venkatraopet Waddial Waddur Wadgaon Waghapur Wankidi Wankidi Wegaon Wellal Yapalguda Yedbid Yellapalli Yellaram Yellawath Yelmal Yenda'
# xy = x.split(' ')
# print(type(xy))
# print(xy)
# z = pd.DataFrame(xy)
# z.to_csv (r'\home\grktechnologies\myfolder\area_names.csv', index = False, header=True)