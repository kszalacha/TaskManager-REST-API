#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, TaskSerializer, TaskSerializerMini, MyTasksSerializer
from .models import User, Task
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class MyTasksViewSet(viewsets.ModelViewSet):
    serializer_class = MyTasksSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return User.objects.filter(username=user)
        return User.objects.none()


