from django.shortcuts import render
from posts.models import *
from rest_framework import viewsets, mixins
from .serializers import *
# Create your views here.
class GenericPostDB(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PostDBSerializer
    queryset = PostDB.objects.all()