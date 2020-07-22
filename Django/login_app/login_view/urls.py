from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from . import views
app_name='login_view'
urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='login')

]