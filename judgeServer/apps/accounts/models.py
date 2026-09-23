import uuid
from django.db import models
# https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django-contrib-auth
from django.contrib.auth.models import AbstractUser

# a table in DB


class User(AbstractUser):
    # Inheritance from AbstractUser
    # a column in table
    # public-facing identifier, so we don't expose the sequential pk
    # would call uuid.uuid4 everytime
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    motto = models.TextField(blank=True)
    user_ip = models.GenericIPAddressField(null=True, blank=True)
