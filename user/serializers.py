from rest_framework import serializers
from user.models import UserAccount, UserImage
from django.contrib.auth.models import User

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password", "confirm_password"]

    def save(self):
        username = self.validated_data["username"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError({"error":"Password Does Not Matched."})
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"error":"Username Already Exist."})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error":"Email Address Already Exists."})
        
        account = User(username=username, first_name=first_name, last_name=last_name, email=email)
        account.set_password(password)
        account.save()
        return account
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    # email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)