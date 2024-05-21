from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    # username = models.CharField(max_length=15)
    # first_name = models.CharField(max_length=25)
    # last_name = models.CharField(max_length=25)
    # email = models.EmailField()
    # password = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class UserImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user/image/", null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"