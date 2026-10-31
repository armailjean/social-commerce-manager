import uuid
from django.conf import settings
from django.db import models
from django.db.models import Q

class Order(models.Model):
    class Source(models.TextChoices):
        FACEBOOK = "facebook", "Facebook"
        WHATSAPP = "whatsapp", "WhatsApp"
        OTHER = "other", "Autre"
    class Status(models.TextChoices):
        DRAFT = "draft", "Brouillon"
        PENDING = "pending", "En attente"
        CONFIRMED = "confirmed", "Confirmée"
        PREPARING = "preparing", "En préparation"
        IN_DELIVERY = "in_delivery", "En livraison"
        DELIVERED = "delivered", "Livrée"
        CANCELLED = "cancelled", "Annulée"
        RETURNED = "returned", "Retournée"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey("stores.Store", on_delete=models.PROTECT, related_name="orders")
    customer = models.ForeignKey("customers.Customer", on_delete=models.PROTECT, related_name="orders")
    order_number = models.CharField(max_length=40)
    source = models.CharField(max_length=20, choices=Source.choices, default=Source.WHATSAPP)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    subtotal = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    shipping_fee = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="created_orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["store", "order_number"], name="uniq_order_number_per_store"),
            models.CheckConstraint(condition=Q(subtotal__gte=0), name="order_subtotal_nonnegative"),
            models.CheckConstraint(condition=Q(discount_amount__gte=0), name="order_discount_nonnegative"),
            models.CheckConstraint(condition=Q(shipping_fee__gte=0), name="order_shipping_nonnegative"),
            models.CheckConstraint(condition=Q(total_amount__gte=0), name="order_total_nonnegative"),
        ]
        indexes = [models.Index(fields=["store", "status", "created_at"]), models.Index(fields=["store", "customer"])]
    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT, related_name="order_items")
    product_name_snapshot = models.CharField(max_length=180)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=14, decimal_places=2)
    unit_cost_snapshot = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    line_discount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    line_total = models.DecimalField(max_digits=14, decimal_places=2)
    class Meta:
        constraints = [
            models.CheckConstraint(condition=Q(quantity__gt=0), name="order_item_quantity_positive"),
            models.CheckConstraint(condition=Q(unit_price__gte=0), name="order_item_price_nonnegative"),
            models.CheckConstraint(condition=Q(unit_cost_snapshot__gte=0), name="order_item_cost_nonnegative"),
            models.CheckConstraint(condition=Q(line_discount__gte=0), name="order_item_discount_nonnegative"),
            models.CheckConstraint(condition=Q(line_total__gte=0), name="order_item_total_nonnegative"),
        ]

class OrderStatusHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey("stores.Store", on_delete=models.PROTECT, related_name="order_status_events")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="status_history")
    old_status = models.CharField(max_length=20, blank=True)
    new_status = models.CharField(max_length=20, choices=Order.Status.choices)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    comment = models.TextField(blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["changed_at"]
        indexes = [models.Index(fields=["store", "order", "changed_at"])]
