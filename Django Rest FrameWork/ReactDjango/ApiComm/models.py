from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#User._meta.get_field('email')._unique = True
class Post(models.Model):
	title=models.CharField(max_length=50)
	post=models.TextField()
	author=models.CharField(max_length=50)
	date_created=models.DateField(default=timezone.now)

	def __str__(self):
		return self.title

CHOICES=(('M','Male'),('F', 'Female'), ('O', 'Other'))

def upload_path(instance, filename):
	return '/'.join(['profile_pic', str(instance.user.username), filename])

class UserModel(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	gender=models.CharField(max_length=1, choices=CHOICES, default='M')
	profile_pic=models.ImageField(blank=True, null=True,upload_to=upload_path)
	def __str__(self):
		return self.user.username
