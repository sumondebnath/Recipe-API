from django.shortcuts import render
from rest_framework import viewsets, permissions
from comment.serializers import CommentSerializer
from comment.models import Comment

# Create your views here.

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")
        recipe_id = self.request.query_params.get("recipe_id")
        # print(user_id, recipe_id)

        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if recipe_id:
            queryset = queryset.filter(recipe_id=recipe_id)
        return queryset