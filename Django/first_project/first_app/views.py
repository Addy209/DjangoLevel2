from django.shortcuts import render
from . import forms
from django.http import HttpResponse as resp

def index(request):
    my_dict={
        'insert_me':"This is coming from Template Tag",
    }
    return render(request,'first_app/index.html',context=my_dict)

# Create your views here.
def form_name_view(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("Valid Data")
            print("Name: "+form.cleaned_data['name'])
    return render(request,'first_app/form.html',{'form':form})