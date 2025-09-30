from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
    }))
    phone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={
        "class": "w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
    }))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "phone", "password1", "password2"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "w-full px-3 py-2 border rounded-md focus:ring-2 focus:ring-indigo-500"}),
            "last_name": forms.TextInput(attrs={"class": "w-full px-3 py-2 border rounded-md focus:ring-2 focus:ring-indigo-500"}),
            "username": forms.TextInput(attrs={"class": "w-full px-3 py-2 border rounded-md focus:ring-2 focus:ring-indigo-500"}),
            "password1": forms.PasswordInput(attrs={"class": "w-full px-3 py-2 border rounded-md focus:ring-2 focus:ring-indigo-500"}),
            "password2": forms.PasswordInput(attrs={"class": "w-full px-3 py-2 border rounded-md focus:ring-2 focus:ring-indigo-500"}),
        }


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Save profile extra field
            Profile.objects.update_or_create(user=user, defaults={
                "phone": self.cleaned_data.get("phone"),
            })
        return user
