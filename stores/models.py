import uuid
from django.conf import settings
from django.db import models

class Store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=180)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="owned_stores")
    phone = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    logo = models.ImageField(upload_to="store_logos/", blank=True)
    currency = models.CharField(max_length=3, choices=[("MGA", "Ariary malagasy")], default="MGA")
    default_language = models.CharField(max_length=2, choices=[("fr", "Français"), ("mg", "Malagasy")], default="fr")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StoreMembership(models.Model):
    class Role(models.TextChoices):
        OWNER = "owner", "Propriétaire"
        MANAGER = "manager", "Gestionnaire"
        COURIER = "courier", "Livreur"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="memberships")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="store_memberships")
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MANAGER)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["store", "user"], name="uniq_membership_store_user")]
        indexes = [models.Index(fields=["user", "is_active"])]
