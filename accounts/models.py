import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=180, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    preferred_language = models.CharField(max_length=2, choices=[("fr", "Français"), ("mg", "Malagasy")], default="fr")

    def __str__(self):
        return self.full_name or self.email or self.username
