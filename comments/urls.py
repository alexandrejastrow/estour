from django.urls import path

from .views import CommentsView

app_name = 'comments'

urlpatterns = [
    path('', CommentsView.as_view(), name='list'),
    path('add/<int:id_place>',
         CommentsView.as_view(), name='addcomments'),
]
