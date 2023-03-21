from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from forms import ProductForm
from products.models import Product
from django.contrib.auth import login, authenticate, logout
from decorators import dashboard_permission

def home(request):
    return render(request, "home.html", {})

def product_page(request):
    products = Product.objects.all()

    context = {
        "products": products
    }
    return render(request, "products.html", context)

def view_single_product(request):
    return render(request, "product_description.html", {})

def cart_page(request):
    return render(request, "cart.html", {})

def user_profile(request):
    # form = ProfileForm(instance=request.user.customer)

    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, request.FILES, instance=request.user.customer)

    #     if form.is_valid():
    #         form.save()

    # context = {
    #     "form": form
    # }

    return render(request, "user_profile.html", {})

# @dashboard_permission 
def admin_dashboard(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('products')
        
    context = {
        "form": form
    }
    return render(request, "admin_dashboard.html", context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products')
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

def user_logout(request):
    logout(request)
    return redirect('login')
