from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import *
from django.views.generic import View, TemplateView, DetailView
from ProductUI.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
class IndexView(View):
    template_name = 'Index/index.html'
    def get(self, request):
        products=Products.objects.all()
        print(products)
        laptop=products.filter(category='Laptop').order_by("-created_date")
        page_ele=Paginator(laptop,5)
        elec_number = request.GET.get('page')
        elec_obj = page_ele.get_page(elec_number)

        mobile=products.filter(category='Mobile').order_by("-created_date")
        page_mo = Paginator(mobile, 5)
        mo_number = request.GET.get('page')
        mo_obj = page_mo.get_page(mo_number)

        earphones=products.filter(category='Earphones').order_by("-created_date")
        page_ep = Paginator(earphones, 5)
        ep_number = request.GET.get('page')
        ep_obj = page_ep.get_page(ep_number)

        other=products.filter(category='Other').order_by("-created_date")
        page_o = Paginator(other, 5)
        o_number = request.GET.get('page')
        o_obj = page_o.get_page(o_number)

        context={
            'laptop':elec_obj,
            'mobile':mo_obj,
            'earphones':ep_obj,
            'other':o_obj
        }
        return render(request, self.template_name,context)



class SignupView(View):
    template_name = 'Login and Signup/signup.html'
    def get(self, request, *args, **kwargs):

        print(1)

        user_form = userForm()
        signup_form = UserInfoForm()
        return render(request,self.template_name,{
            'user_form':user_form,
            'signup_form':signup_form

        })
    def post(self, request):
        user_from=userForm(request.POST)
        user_info=UserInfoForm(request.POST)
        print("Here")
        if user_from.is_valid() and user_info.is_valid():
            user=user_from.save()
            user.set_password(user.password)
            user.save()

            profile=user_info.save()
            profile.user=user
            profile.save()

            pass
        return redirect('/login.html')

class LoginView(View):
    def post(self,request):
        print("Here")
        username=request.POST['username']
        password=request.POST['password']
        keep=request.POST['keep']
        print(username, password, keep)
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
            else:
                return HttpResponse("User Not Active")
        else:
            return HttpResponse("UserName or Password Incorrect")
        return redirect('index')

@login_required
def Signout(request):
    logout(request)
    return redirect('index')

@api_view(['GET'])
def CheckPin(request):

        pinc=request.GET['pincode']
        print(pinc)
        pin=get_object_or_404(area,pk=pinc)
        print(pin)
        return JsonResponse({},status=200)


