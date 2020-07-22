from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class PostSerializers(serializers.ModelSerializer):
	class Meta:
		model=Post
		fields=['id','title','post','author']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['username','password', 'email']

class  UserModelSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserModel
		fields=['gender','profile_pic']

class LoginSeriaizer(serializers.Serializer):
	username=serializers.CharField()
	password=serializers.CharField()