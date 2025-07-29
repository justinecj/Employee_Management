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
            request.user_id = payload['user_id']  # Assuming user_id is in the JWT
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



# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzODEyMzAxLCJpYXQiOjE3NTM4MTIwMDEsImp0aSI6ImJjYzk2YjEwNzBhYTRhM2NiYjlkNzljNWYzOWE2ZDIxIiwidXNlcl9pZCI6IjIifQ.kgDGtMl8hkyImq6ZslTmpnFAHaVbkPKj380VtpNGl_I
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzODEyMzAxLCJpYXQiOjE3NTM4MTIwMDEsImp0aSI6IjdjMWJmNGNmYjgxNTQ3MTdiNTFmMGIzMzcxNzQyZTZhIiwidXNlcl9pZCI6IjIifQ.ncwaYws8hA9w80V-GuTYv07scSEBk5SR1Ux01XPD_wI
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1Mzg5ODQwMSwiaWF0IjoxNzUzODEyMDAxLCJqdGkiOiI0OGFlMDE3OGMyNTc0NjZmOWRiMmY5NzAyMmQyN2Y5MSIsInVzZXJfaWQiOiIyIn0.wIDFU9-YvFQJXAVc7I3Xc824fIz6_O3NJEgV2WeUX0s



# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzODEyODkyLCJpYXQiOjE3NTM4MTI1OTIsImp0aSI6ImIwZWNhNjQ4ZWYwMDQ3Y2E4ZjQwMjdlYzM1ZDcxNGYwIiwidXNlcl9pZCI6IjIifQ.2HRKg3wuBXMTUCb-nrF3sBY0jXj4bEkpE_5IQeMnbxc
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzODEyODkzLCJpYXQiOjE3NTM4MTI1OTMsImp0aSI6Ijc3ZTcyNTI0YzMxNTQyNzZhODhhOGRkNmFiMjVlNzRhIiwidXNlcl9pZCI6IjIifQ.au34C9mEvOgRgeQ8vZNyDJgNnStmhPDYeCZAhTzujbs
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1Mzg5ODk5MiwiaWF0IjoxNzUzODEyNTkyLCJqdGkiOiI4MWYxMjBlZDM4OTg0OGNhODY1NWYzZGVjNTkxMjc3ZCIsInVzZXJfaWQiOiIyIn0.hRyDVudFErnf8UVSx-uPdwjUYlllU48WNMSzvMvCYYk

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzODEyODkyLCJpYXQiOjE3NTM4MTI1OTIsImp0aSI6ImIwZWNhNjQ4ZWYwMDQ3Y2E4ZjQwMjdlYzM1ZDcxNGYwIiwidXNlcl9pZCI6IjIifQ.2HRKg3wuBXMTUCb-nrF3sBY0jXj4bEkpE_5IQeMnbxc