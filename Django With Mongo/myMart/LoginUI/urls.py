from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Signout, name='logout'),
    path('checkpin/',CheckPin, name='pincode')

]