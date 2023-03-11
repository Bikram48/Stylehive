from django.shortcuts import redirect
from django.http import HttpResponse

def dashboard_permission(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            print(request.user.groups.all())
        
        if group == 'Admin':
            return view_func(request, *args, **kwargs)
        if group == 'User':
            return HttpResponse("You aren't allowed to view this page")

    return wrapper_func
