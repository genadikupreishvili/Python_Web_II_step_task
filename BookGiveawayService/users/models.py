from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string


import uuid


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    # email_verification_token = models.CharField(max_length=50, unique=True, null=True, blank=True)
    email_verification_token = models.UUIDField(default=uuid.uuid4, editable=False)

    def generate_email_verification_token(self):
        self.email_verification_token = get_random_string(50)


class Author(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Condition(models.Model):
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.description


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)  # Changed to ForeignKey
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, default="Tbilisi")
    recipient = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='received_books')




