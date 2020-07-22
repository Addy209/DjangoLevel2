
from django.conf.urls import url
from django.urls import path
from . import views
app_name="schoolApp"

urlpatterns = [
    url(r'^$',views.schoolListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.schoolDetailView.as_view(),name='detail'),
    url(r'^create/$',views.SchoolCreateView.as_view(), name="create"),
    path('update/<int:pk>',views.SchoolUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),
]