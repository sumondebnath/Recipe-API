from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comment.views import CommentViewset

router = DefaultRouter()

router.register("list", CommentViewset)


urlpatterns = [
    path("", include(router.urls)),
]