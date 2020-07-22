from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
import datetime
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

class MyApi(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
            mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = TaskSerializer
    print()
    queryset = UserTasks.objects.all()
    authentication_classes = [SessionAuthentication, BaseAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get(self,request, id=None):
        for i in request.META:
            print(i)
        if id:
            return self.retrieve(request)
        return self.list(request)

    def get_queryset(self):
        return UserTasks.objects.filter(user=self.request.user)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)







templateRoot='Tasks/'
def index(request):
    if not request.user.is_authenticated:
        global templateRoot
        return render(request, templateRoot+'index.html')
    else:
        return redirect("/task_list")


def loginView(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            login_form=LoginForm(data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        return redirect('/task_list')
                    else:
                        return HttpResponse('Account Not Active')
                else:
                    return HttpResponse('Invalid Username or password')
            else:
                return HttpResponse('Inappropriate data provided')
        else:
            login_form=LoginForm()
            return render(request, templateRoot+'login.html',{
                'login_form': login_form
            })
    else:
        return redirect("/task_list")



def signupView(request):
    if not request.user.is_authenticated:
        global templateRoot
        registered=False
        if request.method=='POST':
            user_form=UserForm(data=request.POST)
            profile_form=UserProfileInfoForm(data=request.POST)
            print(1)
            if user_form.is_valid() and profile_form.is_valid():
                print(2)
                user=user_form.save()
                user.set_password(user.password)
                user.save()

                profile=profile_form.save(commit=False)
                profile.user=user
                profile.save()
                registered=True
                request=None
                return redirect('/login')
            else:
                messages.add_message(request, messages.WARNING, "User Already Exist")
                return redirect('/signup')
        else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()
            return render(request, templateRoot+'signup.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered
            })
    else:
        return redirect("/task_list")

@login_required
def TaskList(request):
    print(1)
    if request.method=='POST':

        taskadded=request.POST['taskadded']
        deadline=request.POST['deadline']
        print(taskadded)
        UserTasks(user=request.user, task=taskadded, done=False, deadline=deadline).save()
        return redirect('/task_list')
    else:
        print(request.user)
        tasks=UserTasks.objects.filter(user=request.user)
        paginator = Paginator(tasks, 5)
        form=TaskForm()
        pageNumber = request.GET.get('page')
        pageObj = paginator.get_page(pageNumber)
        return render(request,templateRoot+'task_list.html',{
            'form':form,
            'tasks':pageObj
        })

@login_required
def TaskDetail(request, pk):
    task = UserTasks.objects.get(id=pk)
    done=''
    if task.done:
        done='Yes'
    else:
        done='No'
    current=datetime.date.today()

    deadlineOver=''
    if current> task.deadline:
        deadlineOver='Yes'
    else:
        deadlineOver='No'

    return render(request, templateRoot+'task_detail.html', {
        'task':task, 'done': done, 'deadlineOver':deadlineOver
    })

@login_required
def UpdateView(request, pk):
    task = UserTasks.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/task_detail/'+str(pk))
    else:
        form = TaskForm(instance=task)
        return render(request, 'Tasks/task_update.html', {'form': form})

@login_required
def UserLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def DeleteView(request, pk):
    task=UserTasks.objects.get(id=pk)
    
    if request.method=='POST':
        task.delete()
        return redirect("/task_list")

    return render(request,templateRoot+"task_delete.html", {
        'task':task
    })

@login_required
def allTaskView(request):
    if request.user.is_superuser:
        allTask=UserTasks.objects.exclude(user=request.user)
        paginator = Paginator(allTask, 5)
        pageNumber = request.GET.get('page')
        pageObj = paginator.get_page(pageNumber)
        return render(request,templateRoot+"all_user_detail.html",{
            'allTask':pageObj
        })
    else:
        return HttpResponse('''<h2>Sorry! You are not a Superuser</h2>
                            <h3> Please contact an existing Superuser to become one</h3>
                            ''')