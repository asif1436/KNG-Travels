from django.contrib import admin
from admin_page.models import *

# Register your models here.


class  OutStationAdmin(admin.ModelAdmin):
    display = "__all__"

admin.site.register(OutStation, OutStationAdmin)


class  LocalAdmin(admin.ModelAdmin):
    display = "__all__"

admin.site.register(Local, LocalAdmin)


class  AirPortAdmin(admin.ModelAdmin):
    display = "__all__"
    
admin.site.register(AirPort, AirPortAdmin)

class PersionInfoAdmin(admin.ModelAdmin):
    display = "__all__"

admin.site.register(PersionInfo, PersionInfoAdmin)


class CarAdmin(admin.ModelAdmin):
    display = "__all__"

admin.site.register(Car, CarAdmin)


class CardemoAdmin(admin.ModelAdmin):
    display = "__all__"

admin.site.register(Cardemo, CardemoAdmin)

