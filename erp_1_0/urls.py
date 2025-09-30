from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')), 
    path('inventory/', include('inventory.urls')),
    path('purchases/', include('purchases.urls')),
    path('', lambda request: redirect('login'), name='home'),
]

if getattr(settings, "ENVIRONMENT", "development") == "development":
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
