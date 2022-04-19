from django.db import models

from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from places.models import Place
import uuid


def uuid_generator():
    return str(uuid.uuid4())


class User(AbstractUser):

    id = models.UUIDField(
        primary_key=True, default=uuid_generator, editable=False)
    avathar = models.ImageField(upload_to='avatars/', blank=True)


class FavoriteList(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid_generator, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='favorites')
    places = models.ManyToManyField(Place, blank=True)

    def __str__(self):
        return f'Favorites of: {self.user.username}'


def create_user_favorite(sender, instance, created, **kwargs):
    if created:
        FavoriteList.objects.create(user=instance)


def save_user_favorite(sender, instance, **kwargs):
    instance.favorites.save()


post_save.connect(create_user_favorite, sender=User)
post_save.connect(save_user_favorite, sender=User)
