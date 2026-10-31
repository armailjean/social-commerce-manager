import uuid
from django.conf import settings
from django.db import models
from django.db.models import Q

class StockMovement(models.Model):
    class Type(models.TextChoices):
        ENTRY = "entry", "Entrée"
        OUT = "out", "Sortie"
        RESERVE = "reserve", "Réservation"
        RELEASE = "release", "Libération de réservation"
        ADJUSTMENT = "adjustment", "Ajustement"
        RETURN = "return", "Retour"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey("stores.Store", on_delete=models.PROTECT, related_name="stock_movements")
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT, related_name="stock_movements")
    order = models.ForeignKey("orders.Order", null=True, blank=True, on_delete=models.PROTECT, related_name="stock_movements")
    movement_type = models.CharField(max_length=20, choices=Type.choices)
    quantity = models.PositiveIntegerField()
    reason = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.CheckConstraint(condition=Q(quantity__gt=0), name="stock_movement_quantity_positive")]
        indexes = [models.Index(fields=["store", "product", "created_at"])]
