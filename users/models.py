from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avathar = models.ImageField(upload_to='', blank=True)
