from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chat_dashboard(request):
    return HttpResponse("your are on chat dashboard page")
