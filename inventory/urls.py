from django.urls import path
from .views import inventory_list, create_product, delete_product,edit_product, product_list, staff_list, order_list, create_order, create_staff, delete_staff, edit_staff

urlpatterns = [
    path('', inventory_list, name='inventory_list'),
    path('products/create/', create_product, name='create_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('products/', product_list, name='product_list'),
    path('staff/', staff_list, name='staff_list'),
    path('orders/', order_list, name='order_list'),
    path('orders/create/', create_order, name='create_order'),
    path('staff/create/', create_staff, name='create_staff'),
    path('staff/<int:staff_id>/edit/', edit_staff, name='edit_staff'),
    path('staff/<int:staff_id>/delete/', delete_staff, name='delete_staff'),


]
