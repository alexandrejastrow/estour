from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, reverse
from django.db.models import Avg
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Place, CategoryPlace, Rating, Comment
from accounts.models import FavoriteList
import math


NO_RATTING = "Sem avaliações"


def my_floor(number: float):

    if not number:
        return 0

    val = number - math.floor(number)

    if val >= 0.25 and val <= 0.75:
        return math.floor(number) + 0.50
    elif val >= 0.75:
        return math.ceil(number)
    else:
        return math.floor(number)


class PlaceListView(ListView):
    template_name = 'places/place_list.html'
    category = None

    def get_queryset(self):
        queryset = Place.objects.all().order_by('?')
        category_slug = self.kwargs.get('slug')

        if category_slug:
            self.category = get_object_or_404(
                CategoryPlace, slug=category_slug)
            queryset = queryset.filter(categories=self.category)
            return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryPlace.objects.all()
        context['category'] = self.category

        places = Place.objects.all().order_by('?')
        for place in places:
            rating = Rating.objects.all().filter(place=place.id).aggregate(Avg('rating'))

            if not rating['rating__avg']:
                place.rating = NO_RATTING
            else:
                place.rating = my_floor(rating['rating__avg'])
        context['place_list'] = places

        return context


class PlaceDetailView(DetailView):
    template_name = 'places/place_detail.html'

    def get_queryset(self):
        queryset = Place.objects.all().filter(slug=self.kwargs.get('slug'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        place = Place.objects.all().filter(slug=self.kwargs.get('slug'))
        rating = Rating.objects.all().filter(
            place=place.first().id).aggregate(Avg('rating'))

        if not rating['rating__avg']:
            context['rating'] = NO_RATTING
        else:
            context['rating'] = my_floor(rating['rating__avg'])

        context['place'] = self.get_object()
        context['categories'] = CategoryPlace.objects.all()
        return context


def new_comment(request, *args, **kwargs):

    comment = Comment()
    comment.user = request.user
    comment.place = Place.objects.all().filter(id=kwargs.get('id_place')).first()
    comment.comment = request.POST.get('comment')
    comment.save()
    return redirect(reverse('places:place-detail', kwargs={'slug': kwargs.get('slug')}))


def favorite(request, *args, **kwargs):
    my_favorites = FavoriteList.objects.get(user_id=kwargs.get('user_id'))

    if my_favorites.places.filter(id=kwargs.get('place_id')).exists():
        my_favorites.places.remove(kwargs.get('place_id'))
        return HttpResponse('remove')
    else:
        my_favorites.places.add(kwargs.get('place_id'))
        return HttpResponse('add')


def get_favorite(request, *args, **kwargs):
    my_favorites = FavoriteList.objects.get(user_id=kwargs.get('user_id'))

    if my_favorites.places.filter(id=kwargs.get('place_id')).exists():
        return HttpResponse('true')
    else:
        return HttpResponse('false')
