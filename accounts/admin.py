from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User, FavoriteList


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ('username', 'email', 'avathar',
                    'is_superuser', 'is_staff', 'is_active', 'date_joined')


@admin.register(FavoriteList)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user',)
    fieldsets = (
        ('Favorite', {'fields': ('places',)}),
    )
