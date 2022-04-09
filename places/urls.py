from django.urls import path

from .views import PlaceListView, PlaceDetailView

app_name = 'places'

urlpatterns = [
    path('', PlaceListView.as_view(), name='list'),
    path('<slug:slug>/', PlaceDetailView.as_view(), name='detail'),
    path('category/<slug:slug>/', PlaceListView.as_view(), name='list_by_category'),
]
