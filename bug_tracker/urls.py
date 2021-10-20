# https://docs.djangoproject.com/en/3.2/topics/http/urls/

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
