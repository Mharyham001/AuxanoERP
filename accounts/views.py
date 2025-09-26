from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render


def is_admin(user):
    return user.is_superuser or user.groups.filter(name="Admin").exists()

def is_inventory(user):
    return user.groups.filter(name__in=["Inventory Supervisor", "Inventory Staff"]).exists()

def is_purchases(user):
    return user.groups.filter(name__in=["+*Purchases Supervisor", "Purchases Staff"]).exists()


