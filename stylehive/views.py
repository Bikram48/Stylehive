from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from decorators import dashboard_permission

def home(request):
    return render(request, "home.html", {})

def user_profile(request):
    return render(request, "user_profile.html", {})

@dashboard_permission 
def admin_dashboard(request):
    return render(request, "admin_dashboard.html", {})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("User doesn't exist")
      
    return render(request, "login.html", {})

def user_registration(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        "form": form
    }

    return render(request, "register.html", context)
