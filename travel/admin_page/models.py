from django.db import models

# Create your models here.


TRIP_TYPE = (
  ('CFA', 'Car from the Airport'),
  ('CTA', 'Car to the Airport')
)
CHOICES=(('ONE WAY', 'One way'),
  ('Round Trip', 'Round Trip'))

class Cardemo(models.Model):
    cars = models.CharField(max_length=50, null=True, verbose_name="car name")
    img = models.ImageField(upload_to='4wheeler/Images/', null=True, blank=True, verbose_name="Car Image")

    def __str__(self):
        return self.cars
    
    def carimg(self):
        return self.img


class OutStation(models.Model):
    os_trip_type = models.CharField(max_length=50, null=True, blank=True, verbose_name="Trip Type")
    os_from = models.CharField(max_length=100, null=True, blank=True , verbose_name="FROM city -e.g. Wankidi" )
    os_to = models.CharField(max_length=100, null=True, blank=True, verbose_name="TO city -e.g. Hyderabad")
    os_pickup = models.DateField(null=True, blank=True, verbose_name="PICK UP")
    os_return = models.DateField(null=True, blank=True, verbose_name="RETURN")
    os_picktime = models.TimeField(null=True, blank=True, verbose_name="PICK UP AT")
    os_car = models.ForeignKey(Cardemo, null=True, default=Cardemo.cars , on_delete=models.CASCADE)


    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "OutStations"
        verbose_name = "OutStation"

    def __str__(self):
        return self.os_trip_type


class Local(models.Model):
    l_city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Start typing city -e.g. Wankidi")
    l_pickup = models.DateField(null=True, blank=True, verbose_name="PICK UP")
    l_picktime = models.TimeField(null=True, blank=True, verbose_name="PICK UP AT")
    

    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Locals"
        verbose_name = "Local"

    def __str__(self):
        return self.l_city

class AirPort(models.Model):
    ap_city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Start typing city -e.g. Hyderabad")    
    ap_trip = models.CharField(max_length=50, null=True, blank=True, choices=TRIP_TYPE)
    ap_pic_add = models.CharField(max_length=100, null=True, blank=True, verbose_name="Enter your address -e.g. Hyderabad")
    ap_pickup = models.DateField(null=True, blank=True, verbose_name="PICK UP")
    ap_picktime = models.TimeField(null=True, blank=True, verbose_name="PICK UP AT")

    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "AirPorts"
        verbose_name = "AirPort"

    def __str__(self):
        return self.ap_city


class PersionInfo(models.Model):
    p_os = models.ForeignKey(OutStation, null=True, blank=True, on_delete=models.CASCADE)
    p_local = models.ForeignKey(Local, null=True, blank=True, on_delete=models.CASCADE)
    p_ap = models.ForeignKey(AirPort, null=True, blank=True, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=50, null=True, verbose_name="Name")
    p_Phone = models.CharField(max_length=50, null=True, verbose_name="Mobile Number")
    p_emai = models.EmailField(null=True, blank=True, verbose_name="Demo@gmail.com")
    p_address = models.CharField(max_length=100, null=True, blank=True, verbose_name="Exact Drop Location")

    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "PersionInfos"
        verbose_name = "PersionInfo"
    
    def __str__(self):
        return str(self.p_name)

class Car(models.Model):
    c_car = models.CharField(max_length=50, null=True, verbose_name="Select Car")
    c_os = models.ForeignKey(OutStation, null=True, blank=True, on_delete=models.CASCADE)
    c_local = models.ForeignKey(Local, null=True, blank=True, on_delete=models.CASCADE)
    c_ap = models.ForeignKey(AirPort, null=True, blank=True, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name_plural = "Cars"
        verbose_name = "Car"
    
    def __str__(self):
        return self.c_car


