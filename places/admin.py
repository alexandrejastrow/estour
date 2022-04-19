from django.contrib import admin

from .models import Place, CategoryPlace, Rating, Gallery, Photo


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'website',
                    'description', 'latitude', 'longitude', 'created_at', 'update_at')
    list_filter = ('categories',)


@admin.register(CategoryPlace)
class CategoryPlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
