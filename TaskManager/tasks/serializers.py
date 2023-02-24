#from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, User


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'user_key']


class TaskSerializerMini(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    user_tasks = serializers.SerializerMethodField()

    def get_user_tasks(self, username):
        queryset = Task.objects.filter(status=False, user_key_id=username)
        serializer = TaskSerializerMini(instance=queryset, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'user_tasks']


class MyTasksSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'user_tasks']