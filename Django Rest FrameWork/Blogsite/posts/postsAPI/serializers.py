from rest_framework import  serializers
from posts.models import *

class PostDBSerializer(serializers.ModelSerializer):
    class Meta():
        model=PostDB
        fields=('author','title', 'text')

class CommentSerializer(serializers.ModelSerializer):
    class Meta():
        model=Comment
        fields=('author', 'text')
