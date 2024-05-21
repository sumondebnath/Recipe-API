from django.contrib import admin
from user.models import UserAccount, UserImage

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(UserImage)