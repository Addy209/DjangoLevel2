import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','level2Challenge.settings')

import django
django.setup()

from proTwo.models import User
from faker import Faker

fakegen=Faker()
def populate(N=5):
    for entry in range(N):
        
        fake_FN=fakegen.first_name()
        fake_LN=fakegen.last_name()
        fake_EMAIL=fakegen.free_email()

        u=User.objects.get_or_create(first_name=fake_FN, last_name=fake_LN, email=fake_EMAIL)[0]
        u.save()
populate(20)

