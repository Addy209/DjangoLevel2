import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','RestaurantManagingSystem.settings')

import django
django.setup()

import random
from Mainpage.models import Menu
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for entry in range(N):

        fake_dishname=fakegen.name()
        fake_category=fakegen.random_letter()
        fake_price=50

        menu=Menu.objects.get_or_create(dishname=fake_dishname,category=fake_category,price=fake_price)[0]
        

if __name__=='__main__':
    print("Populating")
    populate(20)
    print("Done Populating")