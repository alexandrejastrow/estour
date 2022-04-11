from django.contrib import admin

from .models import CategoryPlace, Place, Rating


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


@admin.register(Rating)
class RatingCategoryPlaceAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'value')
