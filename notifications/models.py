import uuid
from django.db import models

class Notification(models.Model):
    class Channel(models.TextChoices):
        WHATSAPP = "whatsapp", "WhatsApp"
        EMAIL = "email", "E-mail"
        SMS = "sms", "SMS"
    class Status(models.TextChoices):
        QUEUED = "queued", "En attente"
        SENT = "sent", "Envoyée"
        DELIVERED = "delivered", "Distribuée"
        FAILED = "failed", "Échec"
        READ = "read", "Lue"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey("stores.Store", on_delete=models.PROTECT, related_name="notifications")
    order = models.ForeignKey("orders.Order", null=True, blank=True, on_delete=models.SET_NULL, related_name="notifications")
    customer = models.ForeignKey("customers.Customer", null=True, blank=True, on_delete=models.SET_NULL, related_name="notifications")
    channel = models.CharField(max_length=20, choices=Channel.choices, default=Channel.WHATSAPP)
    template_key = models.CharField(max_length=100, blank=True)
    recipient = models.CharField(max_length=180)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.QUEUED)
    provider_message_id = models.CharField(max_length=180, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        indexes = [models.Index(fields=["store", "status", "created_at"])]
