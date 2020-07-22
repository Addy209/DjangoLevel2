from django import forms
from django.core import validators
from Mainpage.models import CustomerDetails, Menu, Sales


class UserInfoForm(forms.ModelForm):
    name = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Customer\'s Name',
                                                         'style': 'margin-left:40px',
                                                         'pattern': '^[A-Za-z ]{1,20}$'}),
                           validators=[validators.MaxLengthValidator(20)],)
    phone = forms.DecimalField(label='',
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                               'id': 'phone',
                                                               'placeholder': 'Customer\'s Phone Number ',
                                                               'style': 'margin-left:30px',
                                                               'pattern': '[7-9][0-9]{9}',
                                                               'title': 'Phone Number should be of 10 digits'}),
                               validators=[validators.RegexValidator(
                                   regex='[7-9][0-9]{9}',
                                   message="phone number not correct"
                               )])
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Customer\'s Email ',
                                                            'style': 'margin-left:30px', }),
                             validators=[validators.EmailValidator])

    class Meta:
        model = CustomerDetails
        fields = '__all__'


class SalesRecord(forms.ModelForm):
    class Meta:
        model = Sales
        exclude = ['date']
