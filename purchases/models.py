from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

class PurchaseRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined')], default='pending')

    def __str__(self):
        return f"{self.item} - {self.quantity} ({self.status})"

class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"PO for {self.item_name} from {self.vendor.name}"

class RequestForMaterials(models.Model):
    MATERIAL_STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    ]

    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=MATERIAL_STATUS, default='pending')

    def __str__(self):
        return f"{self.item_name} - {self.status}"
    
class RequestForQuote(models.Model):
    material_request = models.ForeignKey(RequestForMaterials, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    requested_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()

    def __str__(self):
        return f"RFQ for {self.material_request.item_name} → {self.vendor.name}"


class QuotationReceived(models.Model):
    rfq = models.ForeignKey(RequestForQuote, on_delete=models.CASCADE)
    quoted_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time_in_days = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rfq.vendor.name} quote for {self.rfq.material_request.item_name}"

