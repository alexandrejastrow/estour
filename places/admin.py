from django.contrib import admin

from .models import CategoryPlace, Place, Rating


@admin.register(CategoryPlace)
class CategoryPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'update_at')
    list_filter = ('update_at', 'created_at', 'place')

    fieldsets = (
        ('Category', {
            'fields': ('name',)
        }
        ),
        ('Image', {
            'fields': ('image',)
        }
        ),
    )


@ admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'telephone',
        'latitude',
        'longitude',
        'category',
        'update_at',
    ]
    list_filter = ('category', 'created_at', 'update_at')

    fieldsets = (
        ('Place Name', {
            'fields': ('name',)
        }
        ), ('Description', {
            'fields': ('description',)
        }
        ),
        ('Image', {
            'fields': ('image',)
        }
        ),
        ('Coordinates', {
            'fields': ('latitude', 'longitude',)
        }
        ),
        ('Telephone Contact', {
            'fields': ('telephone',)
        }
        ),
        ('Site', {
            'fields': ('site',)
        }
        ),
    )


@ admin.register(Rating)
class RatingCategoryPlaceAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'value')

    list_filter = ('value',)
