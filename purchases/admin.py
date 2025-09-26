from django.contrib import admin
from .models import (
    Vendor,
    PurchaseRequest,
    PurchaseOrder,
    RequestForMaterials,
    RequestForQuote,
    QuotationReceived
)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'email', 'phone')

@admin.register(PurchaseRequest)
class PurchaseRequestAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'requester', 'status', 'requested_at')
    list_filter = ('status',)
    search_fields = ('item', 'description')

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'vendor', 'quantity', 'status', 'created_at', 'requested_by')
    list_filter = ('status', 'vendor')

@admin.register(RequestForMaterials)
class RequestForMaterialsAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'requester', 'status', 'requested_at')
    list_filter = ('status',)
    search_fields = ('item_name',)

@admin.register(RequestForQuote)
class RequestForQuoteAdmin(admin.ModelAdmin):
    list_display = ('material_request', 'vendor', 'requested_at', 'deadline')
    list_filter = ('vendor',)

@admin.register(QuotationReceived)
class QuotationReceivedAdmin(admin.ModelAdmin):
    list_display = ('rfq', 'quoted_price', 'delivery_time_in_days', 'submitted_at')
    search_fields = ('notes',)
