from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe.views import RecipeViewset

router = DefaultRouter()

router.register("list", RecipeViewset)

urlpatterns = [
    path("", include(router.urls)),
]