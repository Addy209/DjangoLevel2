from django.conf.urls import url
from proTwo import views

urlpatterns=[
    url(r'^signup/',views.signup ,name='signup'),
    url(r'^data/',views.userlist,name='userlist'),
    


]