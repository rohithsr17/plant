from django.shortcuts import render, redirect, Http404, HttpResponse
from django.contrib import messages
import os
from django.conf import settings
from .models import *
from django.core.files.storage import FileSystemStorage


# Create your views here.
def register(request):
    if request.method == "POST":
        use = False
        username = request.POST.get('username')
        try:
            User.objects.get(username=username)
            use = True

        except User.DoesNotExist:
            pass
        if use:
            messages.error(request, "username already exists")
            return redirect('/user_registration.html')
        else:
            user = User()
            user.username = username
            user.name = request.POST.get('name')
            user.date = request.POST.get('dob')
            user.email = request.POST.get('email')
            user.password = request.POST.get('pass')
            user.phone = request.POST.get('phone')
            user.address = request.POST.get('address')
            user.save()
            messages.success(request, "registered successfully")
            return redirect('/user_login.html')
    return render(request, "register.html")


def login(request):
    if "user" in request.session:
        messages.success(request, 'already logged in')
        return redirect('/user_page.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')
            print(0)
            try:
                user = User.objects.get(username=username)
                print(1)
                if user.password != password:
                    print(2)
                    messages.success(request, 'password is wrong')
                    return redirect('/user_login.html')
                request.session['user'] = user.username
                return redirect('/user.html')
            except User.DoesNotExist:
                messages.success(request, 'username does not exist')
                return redirect('/user_login.html')
        return render(request, "login.html", {'name': 'user'})


def page(request):
    if 'user' in request.session:
        return render(request, 'user.html')
    else:
        messages.success(request, 'session already loggedout')
        return redirect('/user_login.html')


def logout(request):
    if 'user' in request.session:
        request.session.pop('user', None)
        messages.success(request, 'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session loggedout')
        return redirect('/user_login.html')

