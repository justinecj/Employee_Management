from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect
from functools import wraps
import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from django.http import HttpResponseRedirect

def jwt_login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        print("Checking JWT token in cookies...")
        token = request.COOKIES.get('access')
        print(token)
        if not token:
            print("No JWT token found in cookies.")
            return redirect('login_page')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(f"Decoded JWT payload: {payload}")
            request.user_id = payload['user_id']  
            print(f"User ID from JWT: {request.user_id}")
            # You can also fetch user here if needed
            # request.user = User.objects.get(id=payload['user_id'])
        except (ExpiredSignatureError, InvalidTokenError):
            print("JWT token is invalid or expired.")
            return redirect('login_page')

        return func(request, *args, **kwargs)
    return wrapper
@never_cache
def login_view(request):
    return render(request, 'login.html')

@never_cache
def register_view(request):
    return render(request, 'register.html')

@never_cache
@jwt_login_required
def dashboard_view(request):
    return render(request, 'index.html')

@never_cache
@jwt_login_required
def change_password_page(request):
    return render(request, 'change_password.html')

@never_cache
@jwt_login_required
def profile_view(request):
    return render(request, "profile.html")

def logout_view(request):
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('access')
    return response

