from django.contrib import admin
from admin_page.models import *
from import_export.admin import ExportActionMixin, ImportExportActionModelAdmin



# Register your models here.

class  CitysAdmin(ImportExportActionModelAdmin):
    list_display = [field.name for field in Citys._meta.get_fields()]

admin.site.register(Citys, CitysAdmin)


class  OutStationAdmin(ImportExportActionModelAdmin):
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

class ProfileAdmin(admin.ModelAdmin):
    display = "__all__"

admin.site.register(Profile, ProfileAdmin)

