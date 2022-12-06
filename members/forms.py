from django.contrib.auth.forms import UserCreationForm
from .models import Members


class RegisterForm(UserCreationForm):
    class Meta:
        model = Members
        fields = ["email", "password1", "password2", "first_name", "last_name"]
