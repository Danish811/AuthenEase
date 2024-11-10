from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


class SignupForm(UserCreationForm):
    email = forms.EmailField(validators=[EmailValidator()])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()
