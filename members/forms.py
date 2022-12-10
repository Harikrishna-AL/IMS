from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from .models import Members


class RegisterForm(UserCreationForm):
    class Meta:
        model = Members
        fields = ["email", "password1", "password2", "first_name", "last_name"]

    email = forms.EmailField(
        label="Email",
        max_length=100,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )
    password1 = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm Password"}
        ),
    )
    first_name = forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = Members
        fields = ["old_password", "new_password1", "new_password2"]

    old_password = forms.CharField(
        label="Old Password",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Old Password"}
        ),
    )
    new_password1 = forms.CharField(
        label="New Password",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "New Password"}
        ),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm New Password"}
        ),
    )
