from django.urls import path

from .views import PlaceListView, PlaceDetailView, favorite, get_favorite, new_comment

app_name = 'places'

urlpatterns = [
    path('', PlaceListView.as_view(), name='place_list'),
    path('favorite/<uuid:user_id>/<uuid:place_id>', favorite),
    path('favorite/get/<uuid:user_id>/<uuid:place_id>', get_favorite),
    path('<slug:slug>/', PlaceDetailView.as_view(), name='place-detail'),
    path('category/<slug:slug>/', PlaceListView.as_view(), name='category-list'),
    path('add/<slug:slug>/<uuid:id_place>', new_comment, name='addcomments'),

]
