from django.db import models
from django.conf import settings


class Comment(models.Model):

    comment = models.TextField()

    place = models.ForeignKey('places.Place', on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'author: {self.author.username}, place: {self.place.name}'

    objects = models.Manager()
