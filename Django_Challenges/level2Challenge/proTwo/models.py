from django.db import models
from django.db.models import Model
# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30, primary_key=True)

    def __str__(self):
        return "Name: "+self.first_name+" AND Email: "+self.email
