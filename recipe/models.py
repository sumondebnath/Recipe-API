from django.db import models
from user.models import UserAccount
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="recipe/images/", null=True, blank=True)

    def __str__(self):
        return self.title