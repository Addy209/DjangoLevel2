from rest_framework import  serializers
from .models import *

class PostDBSerializer(serializers.ModelSerializer):
    class Meta():
        model=PostDB
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta():
        model=Comment
        fields=('author', 'text')
