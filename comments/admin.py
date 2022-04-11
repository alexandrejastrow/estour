from django.contrib import admin

from .models import Comment

# Register your models here.


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'place', 'comment', 'created_at')

    list_filter = ('created_at', 'place')

    fieldsets = (
        ('Author', {
            'fields': ('author',)
        }
        ),
        ('Places', {
            'fields': ('place',)
        }
        ),
        ('Comments', {
            'fields': ('comment', )
        }
        )
    )
