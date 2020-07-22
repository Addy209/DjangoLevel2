from django.shortcuts import render
from django.views.generic import View,DetailView
from django.http import HttpResponseRedirect, Http404, JsonResponse
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import commentForm
from LoginUI.models import Appuser
from .Serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, viewsets
from rest_framework import pagination
from rest_framework.decorators import api_view


# Create your views here.

class ProductDetail(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer 
    pagination_class=pagination.PageNumberPagination


    def list(self, request):
        query=Products.objects.filter(category=request.GET.get('category'))

        page = self.paginate_queryset(query)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)


class SpecsDetails(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    
    serializer_class=SpecsSerializers
    
    def list(self, request):
        query=Specifications.objects.filter(product=request.GET.get('productid'))
        print('Here')
        serializer= self.serializer_class(query, many=True)
        return Response(serializer.data)

class UserReviewDetails(viewsets.GenericViewSet,mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset=UserReview.objects.all()
    serializer_class=UserReviewSerializer
    pagination_class=pagination.PageNumberPagination

    def list(self, request):
        query=UserReview.objects.filter(product=request.GET.get('productid')).order_by("-commented")
        
        page = self.paginate_queryset(query)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    
        
@api_view(['GET'])
def getUserReview(request):
    review=UserReview.objects.filter(user=request.GET.get('user'), product=request.GET.get('productid')).order_by("-commented")[:1]
    serializer=UserReviewSerializer(review, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def handleUpvotes(request,id):
    review=get_object_or_404(UserReview, pk=id)
    print(review)
    data={'upvotes':review.upvotes+1}
    serializer=UserReviewSerializer(review,data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    #print(request.data.get('upvotes'))
    return Response({review.upvotes})


@api_view(['GET'])
def Search(request):
    query=request.GET.get('query')
    result=Products.objects.filter(name__icontains=query)
    serializer=ProductSerializer(result, many=True)
    return Response(serializer.data)
