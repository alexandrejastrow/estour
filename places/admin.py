from django.contrib import admin

from .models import Place, CategoryPlace, Rating, Gallery, Photo, Comment


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'website',
                    'address_url', 'created_at', 'update_at')
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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
