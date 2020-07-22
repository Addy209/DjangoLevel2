from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('signup/',signupView,name='signup'),
    path('login/',loginView,name='login'),
    path('task_list/',TaskList,name='tasklist'),
    path('task_detail/<int:pk>',TaskDetail,name='taskdetail'),
    path('update/<int:pk>',UpdateView, name='update'),
    path('logout/',UserLogout, name='logout'),
    path('delete/<int:pk>',DeleteView,name='delete'),
    path('alltask/',allTaskView, name='alltask'),
    path('api/',MyApi.as_view()),
    path('api/<int:id>',MyApi.as_view()),
]