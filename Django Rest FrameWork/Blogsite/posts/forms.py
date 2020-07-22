from django import forms
from .models import *


class postForm(forms.ModelForm):
    class Meta():
        model=PostDB
        fields=('author', 'title', 'text')
        
        widgets={
            'title':forms.TextInput(attrs={'class': 'textinputclass'}),
            'text':forms.TextInput(attrs={'class': 'editable medium-editor-textarea postcontent'})


        }


class commentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author', 'text')
        widgets={
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.TextInput(attrs={'class': 'editable medium-editor-textarea'})
        }