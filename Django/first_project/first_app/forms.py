from django import forms
from django.core import validators

class FormName(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email=forms.EmailField(validators=[validators.MaxLengthValidator(20)])
    text=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(250)])