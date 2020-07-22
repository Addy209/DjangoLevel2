from  .models import *
from django.contrib.auth.models import User
from django import  forms
from django.core import validators
CHOICES=[('M','Male'),('F', 'Female'),('O', 'Other')]

class userForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','email','password']

class UserInfoForm(forms.ModelForm):
    '''phoneNum=forms.CharField(validators=[validators.RegexValidator(
        regex='[7-9][0-9]{9}',
        message='Phone number not correct'
    )])'''

    class Meta():
        model=Appuser
        fields=['gender','phoneNum','profile_pic']

        widgets={
            'gender':forms.RadioSelect
        }
