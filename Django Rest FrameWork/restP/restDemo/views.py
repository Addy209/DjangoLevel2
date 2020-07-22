from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins, viewsets
from django.shortcuts import get_object_or_404
# Create your views here.

class GenericArticle(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleViewset(viewsets.ViewSet):

    def list(self, request):

        articles=Article.objects.all()
        serializers=ArticleSerializer(articles,many=True)
        return Response(serializers.data)

    def create(self, request):
        serializers = ArticleSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset=Article.objects.all()
        article=get_object_or_404(queryset, pk=pk)
        serializer=ArticleSerializer(article)
        return Response(serializer.data)







class GenericApi(generics.GenericAPIView, mixins.RetrieveModelMixin,
                 mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


    def get(self,request,id=None):
        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self,request, id):
        return self.update(request, id )

    def delete(self, request, id):
        return self.destroy(request,id)




class ApiViewArticle(APIView):
    def get(self,request):
        articles=Article.objects.all()
        serializers=ArticleSerializer(articles,many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers=ArticleSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiViewArticleUD(APIView):
    
    def get_object(self,id):
        try:
            data=Article.objects.get(id=id)
            return data
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        article=self.get_object(id)
        serializers=ArticleSerializer(article)
        return Response(serializers.data)

    def put(self, request, id):
        article=self.get_object(id)
        serializers=ArticleSerializer(article, data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        article=self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def article_list(request):

    if request.method=='GET':
        articles=Article.objects.all()
        serializers=ArticleSerializer(articles,many=True)
        return Response(serializers.data)

    elif request.method=='POST':
        serializers=ArticleSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail(request, pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializers=ArticleSerializer(article)
        return Response(serializers.data)

    elif request.method=='PUT':
        serializers=ArticleSerializer(article,data=request.data)

        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data)
        else:
            JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)