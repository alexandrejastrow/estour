from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


def uuid_generator():
    return str(uuid.uuid4())


class User(AbstractUser):

    id = models.UUIDField(
        primary_key=True, default=uuid_generator, editable=False)
    avathar = models.ImageField(upload_to='avatars/', blank=True)
