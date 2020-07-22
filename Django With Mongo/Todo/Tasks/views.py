from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        val=Tasks.objects.all()
        form=TaskForm()
        return render(request, 'Tasks/index.html',{'val':val,'form':form})

def update(request,pk):
    task = Tasks.objects.get(id=pk)
    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form=TaskForm(instance=task)
        return render(request,'Tasks/update.html',{'form':form})