import uuid
from django.db import models
from django.db.models import Q

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey("stores.Store", on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["store", "name"], name="uniq_category_name_per_store")]
        ordering = ["name"]
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey("stores.Store", on_delete=models.PROTECT, related_name="products")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name="products")
    sku = models.CharField(max_length=80)
    name = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    purchase_price = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=14, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    reserved_quantity = models.PositiveIntegerField(default=0)
    alert_threshold = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["store", "sku"], name="uniq_product_sku_per_store"),
            models.CheckConstraint(condition=Q(purchase_price__gte=0), name="product_purchase_price_nonnegative"),
            models.CheckConstraint(condition=Q(sale_price__gte=0), name="product_sale_price_nonnegative"),
            models.CheckConstraint(condition=Q(reserved_quantity__lte=models.F("stock_quantity")), name="product_reserved_lte_stock"),
        ]
        indexes = [models.Index(fields=["store", "is_active"]), models.Index(fields=["store", "name"])]
    @property
    def available_quantity(self):
        return self.stock_quantity - self.reserved_quantity
    def __str__(self):
        return f"{self.name} ({self.sku})"
