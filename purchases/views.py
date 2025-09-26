from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import RequestForMaterials, Vendor, RequestForQuote, QuotationReceived, PurchaseOrder
from django.contrib import messages


def is_purchases(user):
    return user.groups.filter(name__in=["Purchases Supervisor", "Purchases Staff"]).exists() or user.is_superuser


@login_required
def create_purchase_request(request):
    if request.method == 'POST':
        item = request.POST['item']
        quantity = request.POST['quantity']
        description = request.POST.get('description', '')

        RequestForMaterials.objects.create(
            item_name=item,
            quantity=quantity,
            description=description,
            requester=request.user
        )
        messages.success(request, "Purchase request submitted.")
        return redirect('purchase_request_list')

    return render(request, 'purchases/create_request.html')

@login_required
def rfq(request):
    req = RequestForQuote.objects.all()
    return render(request, 'purchases/rfq_list.html', {'req': req})



@login_required
def create_rfq(request):
    if request.method == 'POST':
        material_id = request.POST['material_request']
        vendor_id = request.POST['vendor']
        deadline = request.POST['deadline']

        material_request = get_object_or_404(RequestForMaterials, id=material_id)
        vendor = get_object_or_404(Vendor, id=vendor_id)

        RequestForQuote.objects.create(
            material_request=material_request,
            vendor=vendor,
            deadline=deadline
        )
        messages.success(request, "RFQ Created successfully.")
        return redirect('create_rfq')

    material_requests = RequestForMaterials.objects.filter(status='approved')
    vendors = Vendor.objects.all()

    return render(request, 'purchases/create_rfq.html', {
        'material_requests': material_requests,
        'vendors': vendors,
    })



@login_required
def quotation_list(request):
    quotations = QuotationReceived.objects.select_related('rfq', 'rfq__material_request', 'rfq__vendor')
    return render(request, 'purchases/quotation_list.html', {
        'quotations': quotations
    })


@login_required
@user_passes_test(is_purchases)
def purchase_request_list(request):
    requests = RequestForMaterials.objects.all()
    return render(request, 'purchases/purchase_list.html', {'requests': requests},)

@login_required
def submit_quotation(request):
    if request.method == 'POST':
        rfq = get_object_or_404(RequestForQuote, id=request.POST['rfq'])
        QuotationReceived.objects.create(
            rfq=rfq,
            quoted_price=request.POST['quoted_price'],
            delivery_time_in_days=request.POST['delivery_time'],
            notes=request.POST.get('notes', '')
        )
        messages.success(request, "Quotation submitted.")
        return redirect('quotation_list')

    rfq = RequestForQuote.objects.all()
    return render(request, 'purchases/submit_quotations.html', {'rfq': rfq})

@login_required
def create_vendor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_person = request.POST.get('contact_person')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')

        if not name or not contact_person:
            messages.error(request, "Name and contact person are required.")
            return render(request, 'purchases/create_vendor.html')

        Vendor.objects.create(
            name=name,
            contact_person=contact_person,
            email=email,
            phone=phone
        )
        messages.success(request, "Vendor created successfully.")
        return redirect('vendor') 

    return render(request, 'purchases/create_vendor.html')

@login_required
def approve_request(request, request_id):
    pr = get_object_or_404(RequestForMaterials, id=request_id)
    pr.status = 'approved'
    pr.save()
    messages.success(request, "Request approved.")
    return redirect('purchase_request_list')

@login_required
def decline_request(request, request_id):
    pr = get_object_or_404(RequestForMaterials, id=request_id)
    pr.status = 'declined'
    pr.save()
    messages.warning(request, "Request declined.")
    return redirect('purchase_request_list')

@login_required
def purchase_order_list(request):
    orders = PurchaseOrder.objects.all()
    return render(request, 'purchases/purchase_order_list.html', {'orders': orders})

@login_required
def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'purchases/vendor.html', {'vendors': vendors})

@login_required
def edit_vendor(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)

    if request.method == 'POST': 
        vendor.name = request.POST.get('username')
        vendor.contact_person = request.POST.get('contact_person')
        vendor.email = request.POST.get('email')
        vendor.phone = request.POST.get('phone')
        vendor.save() 
        messages.success(request, "Vendor updated successfully.")
        return redirect('vendor')
    
    return render(request, 'purchases/edit_vendor.html', {'vendor': vendor})

@login_required
def delete_vendor(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)

    if request.method == 'POST':
        vendor.delete()
        messages.success(request, "Vendor deleted.")
        return redirect('vendor')

    return render(request, 'purchases/delete_vendor.html', {'vendor': vendor})

