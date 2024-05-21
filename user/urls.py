from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import RegistrationViewset, LoginViewset, LogoutViewset, UserAccoutViewset

router = DefaultRouter()
router.register("list", UserAccoutViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("registration/", RegistrationViewset.as_view(), name="register"),
    path("login/", LoginViewset.as_view(), name="login"),
    path("logout/", LogoutViewset.as_view(), name="logout"),
]
