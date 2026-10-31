import uuid
from django.conf import settings
from django.db import models
from django.db.models import Q

class Invoice(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Brouillon"
        ISSUED = "issued", "Émise"
        VOID = "void", "Annulée"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey("stores.Store", on_delete=models.PROTECT, related_name="invoices")
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT, related_name="invoices")
    invoice_number = models.CharField(max_length=50)
    issue_date = models.DateField()
    total_amount = models.DecimalField(max_digits=14, decimal_places=2)
    pdf_file = models.FileField(upload_to="invoices/%Y/%m/", blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["store", "invoice_number"], name="uniq_invoice_number_per_store"),
            models.CheckConstraint(condition=Q(total_amount__gte=0), name="invoice_total_nonnegative"),
        ]
        indexes = [models.Index(fields=["store", "issue_date"])]
