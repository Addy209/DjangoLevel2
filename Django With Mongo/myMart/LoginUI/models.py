from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

CHOICES=(('M','Male'),('F', 'Female'), ('O', 'Other'))

class Appuser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    gender=models.CharField(max_length=1,choices=CHOICES, default='M')
    phoneNum=models.CharField(max_length=10, blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return str(self.user)


class state(models.Model):
    state_name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.state_name


class city(models.Model):
    state_name = models.ForeignKey(state, on_delete=models.CASCADE)
    city_name = models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return self.city_name

class area(models.Model):
    city_name=models.ForeignKey(city, on_delete=models.CASCADE)
    area_name=models.CharField(max_length=20)
    pincode=models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.area_name+" at "+str(self.city_name)+" in "+str(city.objects.values_list('state_name', flat=True).filter(city_name=self.city_name)[0]))


class AppUserAddresses(models.Model):
    user=models.ForeignKey(Appuser, on_delete=models.CASCADE)
    Address_line1=models.CharField(max_length=50)
    Address_line2=models.CharField(max_length=50)
    city_name=models.ForeignKey(city, on_delete=models.CASCADE)
    state_name=models.ForeignKey(state,on_delete=models.CASCADE)
    pincode=models.ForeignKey(area,on_delete=models.CASCADE)



