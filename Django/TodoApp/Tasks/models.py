from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    phoneNo=models.BigIntegerField(unique=True)

    def __str__(self):
        return self.user.username

class UserTasks(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    task=models.CharField(max_length=250)
    done=models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)
    deadline=models.DateField()

    def __str__(self):
        return self.task