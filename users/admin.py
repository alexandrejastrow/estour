from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserCreationForm, UserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'email', 'avathar',
                    'is_superuser', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_active', 'date_joined', 'is_superuser', 'is_staff')

    fieldsets = (
        ('username', {
            'fields': ('username',)
        }
        ),
        ('email', {
            'fields': ('email',)
        }
        ),
        ('avathar', {
            'fields': ('avathar',)
        }
        ),
        ('password', {
            'fields': ('password',)
        }
        ),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
