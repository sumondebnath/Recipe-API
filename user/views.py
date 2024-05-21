from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token

from user.serializers import RegistrationSerializer, LoginSerializer, UserAccountSerializer
from user.models import UserAccount

# Create your views here.

class UserAccoutViewset(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

class RegistrationViewset(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(uid)

            return Response("Registration Confirm.")
        return Response(serializer.errors)
    
class LoginViewset(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            # email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = authenticate(username=username, password=password)
            print(user)
            if user:
                token, other = Token.objects.get_or_create(user=user)
                print(token, other)
                login(request, user)
                return Response({"token":token.key, "user_id":user.id})
            else:
                return Response({"errors":"Invalid Login."})
        return Response(serializer.errors)
    

class LogoutViewset(APIView):
    def post(self, request):
        # token = Token.objects.get(key=token.key)
        # token.delete()
        request.user.auth_token.delete()
        logout(request)
        return Response({'messsage':'Log out successfully.'})