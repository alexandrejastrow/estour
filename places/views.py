from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Place, CategoryPlace
from accounts.models import FavoriteList, User


class PlaceListView(ListView):
    template_name = 'places/place_list.html'
    category = None
    paginate_by = 5

    def get_queryset(self):
        queryset = Place.objects.all().order_by('?')
        category_slug = self.kwargs.get('slug')
        if category_slug:
            self.category = get_object_or_404(
                CategoryPlace, slug=category_slug)
            queryset = queryset.filter(categories=self.category)
            return queryset

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['categories'] = CategoryPlace.objects.all()
            context['category'] = self.category
            return context
        except Exception:
            places = Place.objects.all().order_by('?')
            return {"place_list": places, "categories": CategoryPlace.objects.all()}


class PlaceDetailView(DetailView):
    template_name = 'places/place_detail.html'

    def get_queryset(self):
        queryset = Place.objects.all().filter(slug=self.kwargs.get('slug'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['place'] = self.get_object()
        context['categories'] = CategoryPlace.objects.all()
        return context


def favorite(request, *args, **kwargs):
    my_favorites = FavoriteList.objects.get(user_id=kwargs.get('user_id'))

    if my_favorites.places.filter(id=kwargs.get('place_id')).exists():
        my_favorites.places.remove(kwargs.get('place_id'))
        return HttpResponse('false')
    else:
        my_favorites.places.add(kwargs.get('place_id'))
        return HttpResponse('true')


def get_favorite(request, *args, **kwargs):
    my_favorites = FavoriteList.objects.get(user_id=kwargs.get('user_id'))
    if my_favorites.places.filter(id=kwargs.get('place_id')).exists():
        return HttpResponse('true')
    else:
        return HttpResponse('false')
