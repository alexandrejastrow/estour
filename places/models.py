from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.conf import settings
from autoslug import AutoSlugField
import uuid


def uuid_generator():
    return str(uuid.uuid4())


class CategoryPlace(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid_generator, editable=False)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    banner = models.ImageField(
        upload_to='category_place', blank=True, null=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('places:category-list', kwargs={'slug': self.slug})


class Place(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid_generator, editable=False)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True, null=True)

    categories = models.ManyToManyField(CategoryPlace)

    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    card_img = models.ImageField(upload_to="places", blank=True)
    banner = models.ImageField(upload_to="places", blank=True)

    latitude = models.DecimalField(
        max_digits=14, decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=14, decimal_places=10, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('places:place-detail', kwargs={'slug': self.slug})

    def get_rating(self):
        avg = Rating.objects.filter(place=self.id).aggregate(Avg('rating'))
        print(avg['rating__avg'])
        return avg['rating__avg']

    def get_qtd_rating(self):
        return 2

    def get_highlights(number: int = 3):
        return Place.objects.all().order_by('?')[:number]


class Rating(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid_generator, editable=False)
    choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    rating = models.IntegerField(choices=choices)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.rating} - {self.place.name}'


class Gallery(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid_generator, editable=False)
    place = models.OneToOneField(
        Place, on_delete=models.CASCADE, related_name='gallery')

    def __str__(self):
        return f'Galeria de {self.place.name}'


class Photo(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid_generator, editable=False)
    image = models.ImageField(upload_to='gallery_photos')

    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User: {self.user.username} - Gallery: {self.gallery.place.name}'


def create_place_gallery(sender, instance, created, **kwargs):
    if created:
        Gallery.objects.create(place=instance)


def save_place_gallery(sender, instance, **kwargs):
    instance.gallery.save()


post_save.connect(create_place_gallery, sender=Place)
post_save.connect(save_place_gallery, sender=Place)
