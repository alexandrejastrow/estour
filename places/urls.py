from django.urls import path

from .views import PlaceListView, PlaceDetailView

app_name = 'places'

urlpatterns = [
    path('', PlaceListView.as_view(), name='place_list'),
    path('<slug:slug>/', PlaceDetailView.as_view(), name='place-detail'),
    path('category/<slug:slug>/', PlaceListView.as_view(), name='category-list'),
    path('category/<order>/<slug:slug>/',
         PlaceListView.as_view(), name='order-list'),
]
