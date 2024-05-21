from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer

# Create your views here.

class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["user__username", "user__first_name", "user__last_name", "title", "ingredients", "instructions"]

    def get_queryset(self):
        queryset = super().get_queryset()

        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(user_id = user_id)
        return queryset