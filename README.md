# AuthenEase
This Django project implements a user authentication system, including features such as signup, login, logout, password reset, password change, and user profile views. It is designed with improved error handling, secure password reset links, and user feedback messages.
For Code review, please check ```auth_user/views.py```

## Demo
https://github.com/user-attachments/assets/465dfd0a-0c90-4c72-8c30-bd93c785874c

## Guide
- **User Signup**: Users can create an account.
- **User Login**: Existing users can log in.
- **Password Reset**: Users can reset their passwords via email using secure, one-time links.
- **Password Change**: Logged-in users can change their passwords.
- **Logout**: Users can securely log out.
- **Dashboard and Profile**: Simple profile and dashboard views are accessible to logged-in users.
  
## Advanced features
- Configure EMAIL_BACKEND in settings.py for password reset; Gmail example provided.
- update_session_auth_hash keeps users logged in after password change for convenience.
- Customizable forms (`SignupForm`, `LoginForm`, `ForgotPasswordForm`) allow additional fields.
- try-except blocks prevent errors in critical areas like password reset.
  
## Technologies Used
- **Django**: Django's built-in authentication and form libraries.
- **Python**: Backend logic and form validation.
- **HTML & CSS**: Templates for front-end rendering.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Danish811/AuthenEase.git
   cd AuthenEase
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the Application**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Folder Structure

```plaintext
your_project_name/
├── user_auth/                 # Django app for user authentication
│   ├── forms.py               # Forms for signup, login, forgot password
│   ├── views.py               # Logic for signup, login, password reset, etc.
│   ├── templates/             # HTML templates for each view
│   │   └── user_auth/
│   │       ├── signup.html
│   │       ├── login.html
│   │       ├── forgot_password.html
│   │       ├── change_password.html
│   │       ├── dashboard.html
│   │       └── profile.html
├── manage.py
├── README.md
└── requirements.txt           # Project dependencies
```

