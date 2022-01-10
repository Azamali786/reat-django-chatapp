from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
# Create your views here.

@csrf_exempt
def register(request):
    context = {}
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        mobile_number = data.get("mobile_number")
        email = data.get("email")
        date_of_birth = data.get("date_of_birth")
        password = make_password(data.get("password"))
        User.objects.create(
            username=username,
            mobile_number=mobile_number,
            email=email,
            date_of_birth=date_of_birth,
            password=password,
        )
        return HttpResponse("Registration is successful")
    return HttpResponse("GET method is not allowed")

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        email = None
        username = None
        data = json.loads(request.body)
        password = data.get("password")
        if data.get("email") is not None:
            email = data.get("email")
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("login is successful")

        username = data.get("username")
        user = authenticate(username=email, password=password)
        if data.get("username") is not None:
            login(request, user)
            return HttpResponse("login is successful")
    return HttpResponse("Get method is not allowed here")

@csrf_exempt
def user_logout(request):
    print(request.user)
    logout(request)
    print(request.user)
    return HttpResponse("logged out successfully")