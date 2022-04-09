from django.contrib import admin

from .models import CategoryPlace, Place


@admin.register(CategoryPlace)
class CategoryPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'update_at')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'telephone',
        'latitude',
        'longitude',
        'category',
        'update_at',
    ]
