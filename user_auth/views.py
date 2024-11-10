from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, ForgotPasswordForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'user_auth/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'user_auth/login.html', {'form': form})


def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_mail(
                'Password Reset Request',
                'Click here to reset your password.',
                'admin@example.com',
                [email],
                fail_silently=False,
            )
            return redirect('login')
    else:
        form = ForgotPasswordForm()
    return render(request, 'user_auth/forgot_password.html', {'form': form})


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'user_auth/change_password.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, 'user_auth/dashboard.html', {'user': request.user})


@login_required
def profile_view(request):
    return render(request, 'user_auth/profile.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('login')
