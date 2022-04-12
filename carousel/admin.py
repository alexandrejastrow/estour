from django.contrib import admin
from .models import Carousel


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('slide', 'status',)
    list_filter = ('status',)

    fieldsets = (
        ('Image', {
            'fields': ('slide',)
        }
        ),
        ('Status', {
            'fields': ('status',)
        }
        ),
    )
