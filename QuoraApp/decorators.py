from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


# For register page, we don't want logged in users to access that page
# So, only unauthenticated users allowed
def only_unauthenticated_users_allowed(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('HomePage')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# ONLY admin (group = superuser) will be able to access these pages
def only_admin_allowed(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'normaluser':
            return redirect('HomePage')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


# ONLY NORMAL USERS will be able to view these pages
def only_normal_users_allowed(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'superuser':
            return redirect('/admin')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
