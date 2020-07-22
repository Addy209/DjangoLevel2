from django.shortcuts import render
from django.http import HttpResponse
from proTwo.models import User
from proTwo.forms import NewUserForm
# Create your views here.
def index(request):
    my_dict={
        'heading': 'Welcome to Level 2 Challenge',
        'dir': 'go to /user for all userlist',
        }
    return render(request,'proTwo/index.html',context=my_dict)

def userlist(request):
    user_list=User.objects.order_by('first_name')
    users_dict={'users':user_list}
    return render(request,'proTwo/user.html',context=users_dict)

def signup(request):
    form=NewUserForm()

    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return userlist(request)
        else:
            print('%(request)s is invalid')
    
    return render(request,"proTwo/signup.html",{'form':form})
