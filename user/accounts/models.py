from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class AccessTokenOutStand(models.Model):

    refresh_token = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.access_token