from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, TemplateView
from django.http import HttpResponse
from .models import School, Student
# Create your views here.


def Index(request):
    template_name = 'index.html'
    return render(request, template_name, {'injected': 'This is injected'})


class schoolDetailView(DetailView):
    model = School
    template_name = 'schoolApp/school_detail.html'


class schoolListView(ListView):
    model = School
