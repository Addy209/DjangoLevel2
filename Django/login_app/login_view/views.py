from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm, LoginForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request, 'login_view/index.html')

def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if 'Profile_pic' in request.FILES:
                profile.Profile_pic=request.FILES['Profile_pic']

            profile.save()
            registered=True
            return render(request, 'login_view/registration.html', {'registered':registered})
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
        return render(request, 'login_view/registration.html',{
            'user_form': user_form,
            'profile_form':profile_form,
            'registered':registered
        })

def user_login(request):
    login_form = LoginForm()
    if request.method=='POST':
        print(1)
        login_form= LoginForm(data=request.POST)
        if login_form.is_valid():
            print(2)
            username=login_form.cleaned_data['UserName']
            password=login_form.cleaned_data['Password']
            user=authenticate(username=username, password=password)
            print(3)
            if user:
                print(4)
                if user.is_active:
                    print(5)
                    login(request,user)
                    print(6)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse('Account Not Active')
            else:
                return HttpResponse('Invalid Username or password')
        else:
            return HttpResponse('Inappropriate data provided')
    else:
        return render(request, 'login_view/login.html', {
            'login_form': login_form
        })

@login_required
def specialPage(request):
    return HttpResponse('You are logged in.')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

            
