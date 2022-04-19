from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Place, CategoryPlace


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
