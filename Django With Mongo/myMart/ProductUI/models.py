from django.db import models
from django.utils import timezone
from LoginUI.models import *
from django.contrib.auth.models import User

# Create your models here.
categoryItems=(('Laptop','Laptop'),('Mobile','Mobile'),('Earphones','Earphones'), ('Charger','Charger'),('Desktop','Desktop'),
          ('Smart Watchs','Smart Watches'),('Speakers','Speakers'), ('Other','Other'))
class Products(models.Model):
    category=models.CharField(max_length=20, choices=categoryItems, default='Other')
    name=models.CharField(max_length=200)
    maker=models.CharField(max_length=20)
    model=models.CharField(max_length=20)
    price=models.IntegerField()
    pic=models.ImageField(upload_to='product_pic', blank=True)
    created_date=models.DateField(timezone.now)

    def __str__(self):
        return self.name

class Specifications(models.Model):
    product=models.OneToOneField(Products, related_name='specs', on_delete=models.CASCADE, primary_key=True)
    screen_size=models.CharField(max_length=10, blank=True,)
    processor=models.CharField(max_length=20, blank=True)
    ram=models.CharField(max_length=10, blank=True)
    storage=models.CharField(max_length=10, blank=True)
    storage_type=models.CharField(max_length=10, blank=True)
    battery=models.CharField(max_length=10, blank=True)
    no_of_sims=models.CharField(max_length=10, blank=True)
    wireless=models.CharField(max_length=10, blank=True)
    cable_length=models.CharField(max_length=10, blank=True)
    warrenty=models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.pk)+" "+str(self.product)

class UserReview(models.Model):
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    product=models.ForeignKey(Products, on_delete=models.PROTECT)
    comment=models.TextField()
    commented=models.DateTimeField(default=timezone.now)
    upvotes=models.IntegerField(default=0)

    def __str__(self):
        return self.comment
    



