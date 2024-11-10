from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.contrib import messages
from .forms import SignupForm, LoginForm, ForgotPasswordForm
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Account created successfully. Please log in."))
            return redirect('login')
        else:
            messages.error(request, _("There was an error with your signup. Please try again."))
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
            messages.error(request, _("Invalid username or password."))
    else:
        form = LoginForm()
    return render(request, 'user_auth/login.html', {'form': form})

def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                # Generate token and send reset link
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_link = request.build_absolute_uri(f'/reset_password/{uid}/{token}/')
                email_subject = 'Password Reset Request'
                email_message = render_to_string('user_auth/password_reset_email.html', {
                    'reset_link': reset_link,
                    'user': user,
                })
                send_mail(
                    email_subject,
                    email_message,
                    'admin@example.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, _("A password reset link has been sent to your email."))
            except User.DoesNotExist:
                messages.error(request, _("Email address not found."))
        else:
            messages.error(request, _("Please enter a valid email address."))
    else:
        form = ForgotPasswordForm()
    return render(request, 'user_auth/forgot_password.html', {'form': form})

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Keep the user logged in after password change
            update_session_auth_hash(request, user)
            messages.success(request, _("Your password was successfully updated."))
            return redirect('dashboard')
        else:
            messages.error(request, _("Please correct the error below."))
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
    messages.success(request, _("You have been logged out successfully."))
    return redirect('login')
