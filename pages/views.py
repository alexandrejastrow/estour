from typing import Any, Dict
from django.views.generic import TemplateView

from places.models import Place, CategoryPlace


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        best_places = Place.objects.all().order_by('-rating')[:8]
        categories = CategoryPlace.objects.all()
        context = super().get_context_data(**kwargs)
        highlights = Place.get_highlights(number=4)
        context['categories'] = categories
        context['places'] = best_places
        context['the_best'] = highlights
        return context
