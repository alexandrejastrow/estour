
from django.shortcuts import redirect
from django.views.generic import View
from .models import Comment
from places.models import Place


class CommentsView(View):
    paginate_by = 5

    def post(self, request, id_place):
        comment = request.POST.get('comment')
        if comment:
            data = Comment()
            user = request.user
            place = Place.objects.get(id=id_place)

            data.author = user
            data.place = place

            data.comment = comment
            data.save()

        return redirect(place.get_absolute_url())
