from django.shortcuts import render, redirect
from inventory.models import Staff
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from django.contrib import messages
    


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    modules = [
        {"name": "Inventory", "url": "/inventory/", "desc": "Manage product items"},
        {"name": "Purchases", "url": "/purchases/", "desc": "Manage purchase orders"},
        {"name": "HR", "url": "/#/", "desc": "Human Resources"},
        {"name": "Stock", "url": "/#/", "desc": "Stock level tracking"},
        {"name": "Accounting", "url": "/#/", "desc": "Financial operations"},
        {"name": "CRM", "url": "/#/", "desc": "Customer relationship tracking"},
        {"name": "Sales", "url": "/#/", "desc": "Sales order and invoice management"},
        
    ]
    return render(request, "dashboard.html", {"modules": modules})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
