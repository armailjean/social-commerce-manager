import uuid
from django.conf import settings
from django.db import models

class Delivery(models.Model):
    class Mode(models.TextChoices):
        SELLER = "seller", "Livraison par le vendeur"
        COURIER = "courier", "Livraison par un livreur"
    class Status(models.TextChoices):
        PENDING = "pending", "À organiser"
        ASSIGNED = "assigned", "Livreur affecté"
        SHIPPED = "shipped", "En route"
        DELIVERED = "delivered", "Livrée"
        FAILED = "failed", "Échec"
        CANCELLED = "cancelled", "Annulée"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey("stores.Store", on_delete=models.PROTECT, related_name="deliveries")
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT, related_name="deliveries")
    mode = models.CharField(max_length=10, choices=Mode.choices, default=Mode.SELLER)
    courier = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT, related_name="assigned_deliveries")
    delivery_address = models.TextField()
    delivery_fee = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    failure_reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.mode == self.Mode.SELLER and self.courier_id:
            raise ValidationError({"courier": "Une livraison vendeur ne doit pas avoir de livreur affecté."})
        if self.mode == self.Mode.COURIER and not self.courier_id and self.status in (self.Status.ASSIGNED, self.Status.SHIPPED):
            raise ValidationError({"courier": "Un livreur est requis pour cet état."})
        if self.delivery_fee < 0:
            raise ValidationError({"delivery_fee": "Les frais ne peuvent pas être négatifs."})
