from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home")

def user_login(request):
    return render(request, "login.html", {})

def user_registration(request):
    return render(request, "register.html", {})