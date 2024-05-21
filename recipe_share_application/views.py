from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets, permissions


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]