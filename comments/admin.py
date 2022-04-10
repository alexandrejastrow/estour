from django.contrib import admin

from .models import Comment

# Register your models here.


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'place', 'comment', 'created_at')
