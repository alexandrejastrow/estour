from django.urls import path

from .views import PlaceListView, PlaceDetailView

app_name = 'places'

urlpatterns = [
    path('', PlaceListView.as_view(), name='places'),
    path('<slug:slug>/', PlaceDetailView.as_view(), name='place_detail'),
    path('category/<slug:slug>/', PlaceListView.as_view(), name='category_place'),
]
