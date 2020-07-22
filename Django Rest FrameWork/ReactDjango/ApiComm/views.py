from rest_framework import viewsets,mixins
from .serializers import *
from .models import *
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.response import  Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .decorators import *

class GenericPost(viewsets.GenericViewSet,
	mixins.ListModelMixin,
	mixins.RetrieveModelMixin,
	mixins.CreateModelMixin,
	mixins.UpdateModelMixin, 
	mixins.DestroyModelMixin):
	queryset = Post.objects.all()
	serializer_class = PostSerializers
	permission_classes=[IsAuthenticated,IsAdminUser]
	authentication_classes=[TokenAuthentication]

class LoginView(APIView):
	def post(self,request):
		print(request.data)
		login_ser=LoginSeriaizer(data=request.data)
		if login_ser.is_valid():
			username=login_ser.validated_data['username']
			password=login_ser.validated_data['password']
			print(username,password)
			user=authenticate(username=username, password=password)
			if user and user.is_active:
				token, created=Token.objects.get_or_create(user=user)
				print(token, created)
				return Response({"token":token.key},status=200)
			else:
				raise Exception("Invalid User")

class SignupView(APIView):
	def sendEmail(user):
		myuser=get_object_or_404(User,pk=user.id)
		myuser.is_active=True
		myuser.is_staff=True
		myuser.save()
		#myuser.staff=True

	def post(self, request):
		print(request.data)
		user=UserSerializer(data=request.data)
		user_model=UserModelSerializer(data=request.data)
		print(1)
		if user.is_valid() and user_model.is_valid():

			user_ser=user.save()
			print(type(user_ser))
			user_ser.set_password(user_ser.password)
			#user_ser.is_active=False
			user_ser.save()
			profile=user_model.save(user=user_ser)
			token, created=Token.objects.get_or_create(user=user_ser)
			return Response({"token":token.key},status=200)
		else:
			return Response({"error":user_model.errors}, status=500)

@api_view(['GET'])
@checkIfActivated
def ActivateUsers(user):
	user.is_active=True
	user.auth_token.delete()
	user.save()
	token=Token.objects.create(user=user)
	return Response({"token":token.key})
    
