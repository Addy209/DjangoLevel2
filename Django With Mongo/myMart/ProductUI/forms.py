from django import forms
from .models import *

class commentForm(forms.ModelForm):
    class Meta():
        model=UserReview
        fields=['comment']
        widgets={
            'comment':forms.TextInput(attrs={'class':'form-control'})
        }