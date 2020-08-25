from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
advance=[('25', '25'), ('50', '50'), ('75', '75'), ('100', '100'),]


class PersionInfo(models.Model):
    p_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)   
    p_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Name")
    p_Phone = models.CharField(max_length=50, null=True, blank=True, verbose_name="Mobile Number")
    p_email = models.EmailField(null=True, blank=True, verbose_name="Demo@gmail.com")
    p_address = models.CharField(max_length=100, null=True, blank=True, verbose_name="Exact Drop Location (Optional)")
    p_order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)

    
    p_created_on = models.DateTimeField(auto_now_add=True)
    P_updated_on = models.DateTimeField(auto_now=True)
    
    # def save(self, *args, **kwargs):
    #     print(self.id)
    #     print(self.p_order_id)
    #     print(self.p_created_on)
    #     print(self.p_name)
    #     if self.p_order_id is None and self.p_created_on and self.id:
    #         self.p_order_id = self.p_created_on.strftime('KNG%Y%m%dODR') + str(self.id)
    #         super(PersionInfo, self).save(*args, **kwargs) 

    class Meta:
        verbose_name_plural = "PersionInfos"
        verbose_name = "PersionInfo"
    
    def __str__(self):
        return str(self.p_name)
    
    
    

    
class Cardemo(models.Model):
    cars = models.CharField(max_length=50, null=True, blank=True, verbose_name="car name")
    img = models.ImageField(upload_to='4wheeler/Images/', null=True, blank=True, verbose_name="Car Image")
    ac_price = models.FloatField(null=True, blank=True, verbose_name="Car Ac Price")
    without_ac_price = models.FloatField(null=True, blank=True, verbose_name="Car Without Ac Price")
    advance = models.CharField(max_length=50, null=True, blank=True, choices=advance, verbose_name="Adavnce Payment")

    def __str__(self):
        return self.cars

class Car(models.Model):
    c_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    c_car = models.ForeignKey(Cardemo, default=0, null=True, on_delete=models.CASCADE)
    c_ac_type = models.CharField(max_length=50, null=True, verbose_name="AC Type")    
    c_amount = models.FloatField( null=True, blank=True)
    c_advance = models.FloatField( null=True, blank=True)

    
    class Meta:
        verbose_name_plural = "Cars"
        verbose_name = "Car"
    
    def __str__(self):
        return str(self.c_car)



class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

class OutStation(models.Model):
    os_user = models.ForeignKey(User, related_name='os', null=True, blank=True, on_delete=models.CASCADE)
    os_trip_type = models.CharField(max_length=50, null=True, blank=True, verbose_name="Trip Type")
    os_from = models.CharField(max_length=100, null=True, blank=True , verbose_name="FROM city -e.g. Wankidi" )
    os_to = models.CharField(max_length=100, null=True, blank=True, verbose_name="TO city -e.g. Hyderabad")
    os_pickup = models.DateField(null=True, blank=True, verbose_name="PICK UP")
    os_return = models.DateField(null=True, blank=True, verbose_name="RETURN")
    os_picktime = models.CharField(max_length=100,null=True, blank=True, verbose_name="PICK UP AT")
    os_car = models.ForeignKey(Car, null=True, blank=True, on_delete=models.CASCADE)
    os_persional_info = models.ForeignKey(PersionInfo, null=True, blank=True, on_delete=models.CASCADE)
    

    os_status = models.BooleanField(default=True)
    os_created_on = models.DateTimeField(auto_now_add=True)
    os_updated_on = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name_plural = "OutStations"
        verbose_name = "OutStation"
    
    def __str__(self):
        return str(self.os_user)
    
class Local(models.Model):
    l_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    l_from = models.CharField(max_length=100, null=True, blank=True, verbose_name="From -e.g. Wankidi")
    l_to = models.CharField(max_length=100, null=True, blank=True, verbose_name="To -e.g. Mancherial")
    l_pickup = models.DateField(null=True, blank=True, verbose_name="PICK UP")
    l_picktime = models.CharField(max_length=100,null=True, blank=True, verbose_name="PICK UP AT")
    l_return = models.DateField(null=True, blank=True, verbose_name="RETURN")
    l_car = models.ForeignKey(Car, null=True, blank=True, on_delete=models.CASCADE)
    l_persional_info = models.ForeignKey(PersionInfo, null=True, blank=True, on_delete=models.CASCADE)
    

    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Locals"
        verbose_name = "Local"

    def __str__(self):
        return str(self.l_user)

class AirPort(models.Model):
    ap_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    ap_city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Airport Address -e.g. (RGIA) Rajiv Gandhi International Airport")    
    ap_trip = models.CharField(max_length=50, null=True, blank=True, verbose_name="Trip Type")
    ap_pic_add = models.CharField(max_length=100, null=True, blank=True, verbose_name="Your Address -e.g. Wankidi")
    ap_pickup = models.DateField(null=True, blank=True, verbose_name="PICK UP")
    ap_picktime = models.CharField(max_length=100,null=True, blank=True, verbose_name="PICK UP AT")
    ap_return = models.DateField(null=True, blank=True, verbose_name="RETURN")
    ap_car = models.ForeignKey(Car, null=True, blank=True, on_delete=models.CASCADE)
    ap_persional_info = models.ForeignKey(PersionInfo, null=True, blank=True, on_delete=models.CASCADE)

    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "AirPorts"
        verbose_name = "AirPort"

    def __str__(self):
        return str(self.ap_user)


GENDER=[('Male', 'Male'), ('Female', 'Female')]    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, null=True, blank=True, choices=GENDER, verbose_name="Gender")
    phone = models.CharField(max_length=10, null=True, blank=True, verbose_name="Phone No.")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True, verbose_name="Profile Image")

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("created")
        
@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created==False:
        instance.profile.save()
        print("updated  ")


class City(models.Model):
    city_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="City")
    airport_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Airport_name")


    class Meta:
        verbose_name_plural = "Cities"
        verbose_name = "City"

    def __str__(self):
        return str(self.city_name)