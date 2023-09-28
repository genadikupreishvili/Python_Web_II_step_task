from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # თუ დამჭირდა დამატებით ველებს დავამატებ აქ
    phone_number = models.CharField(max_length=15, null=True, blank=True)
