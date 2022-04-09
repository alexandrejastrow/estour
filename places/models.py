from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

from autoslug import AutoSlugField


class CategoryPlace(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name',
                         unique=True, always_update=False)
    image = models.ImageField(
        upload_to='places/categories/%Y/%m/%d/', blank=True)

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


class Place(models.Model):

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name',
                         unique=True, always_update=False)

    description = models.TextField()
    image = models.ImageField(upload_to='places/%Y/%m/%d/', blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    site = models.URLField(blank=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)

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
