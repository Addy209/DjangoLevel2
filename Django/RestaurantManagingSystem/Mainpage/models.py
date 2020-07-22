from django.db import models
from datetime import timezone
# Create your models here.


class CustomerDetails(models.Model):
    name = models.CharField(max_length=20)
    phone = models.BigIntegerField(primary_key='true')
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name


class Menu(models.Model):
    dishname = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.dishname


class Sales(models.Model):
    name = models.CharField(max_length=30)
    phone = models.ForeignKey(CustomerDetails, on_delete=models.PROTECT)
    order = models.CharField(max_length=300)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
