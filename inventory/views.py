from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Category, Order, Staff 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User


def is_inventory(user):
    return user.groups.filter(name__in=["Inventory Supervisor", "Inventory Staff"]).exists()



@login_required
@user_passes_test(is_inventory)
def inventory_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/base_inventory.html', {'products': products})

@login_required
@user_passes_test(is_inventory)
def create_product(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        new_category = request.POST.get('new_category', '').strip()

        if new_category:  
            
            category_instance, created = Category.objects.get_or_create(name=new_category)
        elif category_id:  
            category_instance = Category.objects.get(id=category_id)
        else:
            category_instance = None  

        Product.objects.create(
            name=request.POST['name'],
            category=category_instance,
            description=request.POST.get('description', ''),
            quantity=request.POST['quantity'],
            unit_price=request.POST['unit_price']
        )

        messages.success(request, "Product added successfully.")
        return redirect('product_list')

    categories = Category.objects.all()
    return render(request, 'inventory/create_product.html', {'categories': categories})

@login_required
@user_passes_test(is_inventory)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        product.name = request.POST['name']
        product.category = Category.objects.get(id=request.POST['category'])
        product.description = request.POST['description']
        product.quantity = request.POST['quantity']
        product.unit_price = request.POST['unit_price']
        product.save()
        return redirect('product_list')

    return render(request, 'inventory/edit_product.html', {'product': product, 'categories': categories})

@login_required
@user_passes_test(is_inventory)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('inventory_list')

    return render(request, 'inventory/delete_product.html', {'product': product})

@login_required
@user_passes_test(is_inventory)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

@login_required
@user_passes_test(is_inventory)
def order_list(request):
    if request.user.is_superuser:
        orders = Order.objects.all()
    else:
        staff = Staff.objects.get(user=request.user)
        orders = Order.objects.filter(staff=staff)

    return render(request, 'inventory/order_list.html', {'orders': orders})

@login_required
@user_passes_test(is_inventory)
def create_order(request):
    products = Product.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        Order.objects.create(
            product_id=request.POST['product'],
            quantity=request.POST['quantity'],
            staff_id=request.POST['staff'],
            status='pending'
        )
        messages.success(request, "Order created.")
        return redirect('order_list')

    return render(request, 'inventory/create_order.html', {'products': products, 'staff': staff})

@login_required
@user_passes_test(is_inventory)
def create_staff(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        role = request.POST.get('role')
        phone = request.POST.get('phone', '')  

        if not user_id:
            messages.error(request, "Name is required.")
            users = User.objects.all()
            return render(request, 'inventory/create_staff.html', {'users': users})

        Staff.objects.create(
            user_id=user_id,
            role=role,
            phone=phone,
        )
        messages.success(request, "Staff member added.")
        return redirect('staff_list')

    
    users = User.objects.all()  
    return render(request, 'inventory/create_staff.html', {'users': users})

@login_required
@user_passes_test(is_inventory)
def edit_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    if request.method == 'POST':
        staff.role = request.POST['role']
        staff.phone = request.POST['phone']
        staff.save()
        messages.success(request, "Staff updated.")
        return redirect('staff_list')

    return render(request, 'inventory/edit_staff.html', {'staff': staff})

@login_required
@user_passes_test(is_inventory)
def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    if request.method == 'POST':
        staff.delete()
        messages.success(request, "Staff deleted.")
        return redirect('staff_list')

    return render(request, 'inventory/delete_staff.html', {'staff': staff})

@login_required
@user_passes_test(is_inventory)
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'inventory/staff_list.html', {'staff': staff})