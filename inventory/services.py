from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import F
from products.models import Product
from orders.models import Order, OrderStatusHistory
from inventory.models import StockMovement

@transaction.atomic
def confirm_order(*, order_id, store_id, actor):
    # L'appelant doit vérifier l'appartenance active de actor à store_id.
    order = Order.objects.select_for_update().filter(id=order_id, store_id=store_id).first()
    if order is None:
        raise ValidationError("Commande introuvable pour cette boutique.")
    if order.status == Order.Status.CONFIRMED:
        return order  # Évite une seconde réservation.
    if order.status not in (Order.Status.DRAFT, Order.Status.PENDING):
        raise ValidationError("État de commande incompatible avec la confirmation.")
    items = list(order.items.select_related("product").order_by("product_id"))
    if not items:
        raise ValidationError("Impossible de confirmer une commande sans article.")
    product_ids = sorted({item.product_id for item in items}, key=str)
    locked = {
        p.id: p for p in Product.objects.select_for_update()
        .filter(id__in=product_ids, store_id=store_id, is_active=True).order_by("id")
    }
    if len(locked) != len(product_ids):
        raise ValidationError("Produit invalide ou appartenant à une autre boutique.")
    required = {}
    for item in items:
        if item.quantity <= 0:
            raise ValidationError("La quantité doit être positive.")
        required[item.product_id] = required.get(item.product_id, 0) + item.quantity
    for pid, qty in required.items():
        if locked[pid].available_quantity < qty:
            raise ValidationError(f"Stock insuffisant pour {locked[pid].name}.")
    for pid, qty in required.items():
        product = locked[pid]
        Product.objects.filter(id=pid, store_id=store_id).update(reserved_quantity=F("reserved_quantity") + qty)
        StockMovement.objects.create(
            store_id=store_id, product=product, order=order,
            movement_type=StockMovement.Type.RESERVE, quantity=qty,
            reason=f"Réservation commande {order.order_number}", created_by=actor
        )
    old = order.status
    order.status = Order.Status.CONFIRMED
    order.save(update_fields=["status", "updated_at"])
    OrderStatusHistory.objects.create(store_id=store_id, order=order, old_status=old, new_status=order.status, changed_by=actor)
    return order
