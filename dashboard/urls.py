from django.urls import path
from .views import dashboard_view, login_view, logout_view, register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]

