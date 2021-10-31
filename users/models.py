from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):  # add timestamp mixin
    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('users:update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('users:delete', kwargs={'pk': self.pk})


# class Profile(models.Model):
# 	avatar = models.CharField(max_length=260, default=get_random_avatar_picture())
