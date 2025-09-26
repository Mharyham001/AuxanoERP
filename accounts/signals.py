from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver

from inventory.models import Product, Order, Staff
from purchases.models import PurchaseOrder, Vendor


@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    # --- Create Groups ---
    admin_group, _ = Group.objects.get_or_create(name="Admin")

    inventory_supervisor_group, _ = Group.objects.get_or_create(name="Inventory Supervisor")
    inventory_staff_group, _ = Group.objects.get_or_create(name="Inventory Staff")

    purchases_supervisor_group, _ = Group.objects.get_or_create(name="Purchases Supervisor")
    purchases_staff_group, _ = Group.objects.get_or_create(name="Purchases Staff")

    # --- Inventory Permissions ---
    inventory_models = [Product, Order, Staff]
    for model in inventory_models:
        ct = ContentType.objects.get_for_model(model)
        perms = Permission.objects.filter(content_type=ct)
        inventory_supervisor_group.permissions.add(*perms)
        inventory_staff_group.permissions.add(*perms)

    # --- Purchases Permissions ---
    purchases_models = [PurchaseOrder, Vendor]
    for model in purchases_models:
        ct = ContentType.objects.get_for_model(model)
        perms = Permission.objects.filter(content_type=ct)
        purchases_supervisor_group.permissions.add(*perms)
        purchases_staff_group.permissions.add(*perms)

    # --- Admin gets everything automatically (or leave them as superuser) ---
    # No need to assign since superusers bypass permissions
