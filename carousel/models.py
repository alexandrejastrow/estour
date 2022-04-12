from django.db import models


class Carousel(models.Model):

    slide = models.ImageField(upload_to='')
    status = models.BooleanField(default=False)

    objects = models.Manager()
