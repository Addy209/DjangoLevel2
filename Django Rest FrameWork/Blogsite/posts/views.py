from django.shortcuts import render, redirect ,get_object_or_404
from django.utils import timezone
from django.views.generic import (TemplateView, CreateView, UpdateView, ListView, DetailView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import *
from .forms import *
from rest_framework.decorators import api_view

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = PostDB
    def get_queryset(self):
        return PostDB.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = PostDB

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'posts/postdb_detail.html'
    form_class = postForm
    model = PostDB

class UpdatePostView(LoginRequiredMixin ,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'posts/postdb_detail.html'
    form_class = postForm
    model = PostDB

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = PostDB
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    template_name = 'posts/postdb_draft_list.html'
    login_url = '/login/'
    redirect_field_name = 'posts/postdb_list.html'
    model = PostDB

    def get_queryset(self):
        return PostDB.objects.filter(published_date__isnull=True).order_by('-created_date')


########################################################################################################################
########################################################################################################################
########################################################################################################################

@login_required
def add_comment_to_post(request, pk):
    pst=get_object_or_404(PostDB, pk=pk)
    if request.method=='POST':
        form=commentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=pst
            comment.save()
            return redirect('post_detail', pk=pst.pk)
    else:
        form=commentForm()
    
    return render(request, 'posts/comment_form.html', {'form':form})

@login_required
def approve_comment(request,pk):

    comment=get_object_or_404(Comment,pk=pk)
    print(pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def remove_comment(request,pk):
    comment=get_object_or_404(Comment, pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@api_view(['GET'])
@login_required
def publish_post(request, pk):
    posts=get_object_or_404(PostDB,pk=pk)
    posts.publish()
    return redirect('post_detail', pk=pk)

########################################################################################################################
#                                           Rest Framework Code                                                        #
########################################################################################################################
from rest_framework import viewsets, mixins
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Create your views here.
class GenericPostDB(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PostDBSerializer
    queryset = PostDB.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class DraftListApi(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = PostDBSerializer
    queryset = PostDB.objects.filter(published_date__isnull=True).order_by('-created_date')
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]