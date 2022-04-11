from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from django.db.models import Avg
from django.conf import settings
from autoslug import AutoSlugField


class CategoryPlace(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name',
                         unique=True, always_update=False)
    image = models.ImageField(
        upload_to='', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category Place'
        verbose_name_plural = 'Categories Places'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('places:list_by_category', kwargs={'slug': self.slug})

    @property
    def get_filename(self):
        if self.image:
            return self.image.name


class Place(models.Model):

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name',
                         unique=True, always_update=False)

    description = models.TextField()
    image = models.ImageField(upload_to='', blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    site = models.URLField(blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    category = models.ForeignKey(CategoryPlace, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('places:detail', kwargs={'slug': self.slug})

    def get_rating(self):
        rating = Rating.objects.all().filter(place=self.id).aggregate(Avg('value'))
        rating['qtd_ratings'] = Rating.objects.all().filter(
            place=self.id).count()
        return [rating['qtd_ratings'], rating['value__avg']]


class Rating(models.Model):
    value = models.IntegerField(
        choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.user.username} - {self.place.name} - {self.value}'
