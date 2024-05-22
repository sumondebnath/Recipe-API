from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets, permissions


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     user_id = self.request.query_params.get("user_id")
    #     if user_id:
    #         queryset = queryset.filter(user_id = user_id)
    #     return queryset