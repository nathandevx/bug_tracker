from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


# class Profile(models.Model):
# 	avatar = models.CharField(max_length=260, default=get_random_avatar_picture())
