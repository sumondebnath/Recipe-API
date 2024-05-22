from django.shortcuts import render
from rest_framework import viewsets, permissions
from comment.serializers import CommentSerializer
from comment.models import Comment

# Create your views here.

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]