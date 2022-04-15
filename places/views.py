from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Place, CategoryPlace


class PlaceDetailView(DetailView):

    def get_queryset(self):
        queryset = Place.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RatingVoteView():

    def get_queryset(self):
        queryset = Place.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PlaceListView(ListView):
    category = None
    paginate_by = 5

    def get_queryset(self):
        queryset = Place.objects.all().order_by('?')

        category_slug = self.kwargs.get('slug')
        if category_slug:
            self.category = get_object_or_404(
                CategoryPlace, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = CategoryPlace.objects.all()

        return context
