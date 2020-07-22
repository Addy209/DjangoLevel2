from django.shortcuts import render
from django.views.generic import (View, ListView, DetailView, TemplateView,
                                    CreateView,UpdateView, DeleteView)

from django.http import HttpResponse
from .models import School, Student
from django.urls import reverse_lazy
# Create your views here.


class Index(TemplateView):
    template_name = 'schoolApp/index.html'
    def get_context_data(slef, **kwargs):
        context=super().get_context_data(**kwargs)
        context['injected']='This text is injected'
        return context


class schoolDetailView(DetailView):
    model = School
    template_name = 'schoolApp/school_detail.html'


class schoolListView(ListView):
    model = School

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = School


class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = School

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("schoolApp:list")
