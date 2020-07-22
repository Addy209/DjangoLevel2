from rest_framework import serializers
from .models import UserTasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta():
        model=UserTasks
        exclude=('user',)