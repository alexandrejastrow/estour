from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User, FavoriteList


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    pass


@admin.register(FavoriteList)
class FavoriteAdmin(admin.ModelAdmin):
    pass
