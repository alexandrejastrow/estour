import requests
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Place, CategoryPlace


class PlaceDetailView(DetailView):
    queryset = Place.objects.all()


class PlaceListView(ListView):
    category = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Place.objects.all()
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

    def download(request, id):
        obj = get_object_or_404(Place, id=id)
        file_data = None

        if obj.image:
            file_data = obj.image.url
        if file_data:
            resp = requests.get(file_data)
            filename = file_data.split('/')[-1]
            response = HttpResponse(resp.content, content_type='image/jpeg')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
        return Http404
