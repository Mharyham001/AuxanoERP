from django.urls import path
from .  import views

urlpatterns = [
    path('', views.purchase_request_list, name='purchase_request_list'),
    path('request/', views.create_purchase_request, name='create_purchase_request'),
    path('rfq/', views.rfq, name='rfq'),
    path('rfq/create/', views.create_rfq, name='create_rfq'),
    path('quotations/', views.quotation_list, name='quotation_list'),
    path('quotation/submit/', views.submit_quotation, name='submit_quotation'),
    path('vendor/new/', views.create_vendor, name='create_vendor'),
    path('vendors/', views.vendor_list, name='vendor'),
    path('vendors/<int:pk>/edit/', views.edit_vendor, name='edit_vendor'),
    path('vendors/<int:pk>/delete/', views.delete_vendor, name='delete_vendor'),
    path('request/<int:request_id>/approve/', views.approve_request, name='approve_request'),
    path('request/<int:request_id>/decline/', views.decline_request, name='decline_request'),
    path('orders/', views.purchase_order_list, name='purchase_order_list'),

]
