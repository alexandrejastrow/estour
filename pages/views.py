from django.shortcuts import render
from django.views import View
# Create your views here.
from places.models import CategoryPlace, Place


class HomePageView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        categories = CategoryPlace.objects.all()
        places = Place().get_highlights()
        return render(request, self.template_name, {'categories': categories, 'places': places})
