from django.shortcuts import render
from django.views import View
# Create your views here.
from places.models import CategoryPlace, Place
from carousel.models import Carousel


class HomePageView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        categories = CategoryPlace.objects.all()
        destaques = Place().get_highlights()[:15]

        slides = Carousel.objects.all().filter(status=True)[:10]
        return render(request, self.template_name,
                      {'categories': categories,
                       'slides': slides,
                       'destaques': destaques
                       }
                      )
