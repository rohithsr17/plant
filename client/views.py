from django.shortcuts import render, redirect, Http404, HttpResponse
from django.contrib import messages
import os
from django.conf import settings
from .models import *
from user.models import *


# Create your views here.
def register(request):
        use=False
        if request.method == "POST":
            username = request.POST.get('username')
            try:
                use= Client.objects.get(username=username)
            except:
                pass
            if use is not False:
                messages.error(request, "username already exists")
                return redirect('/client_registration.html')
            else:
                user = Client()
                user.username = username
                user.name = request.POST.get('name')
                user.date = request.POST.get('dob')
                user.email = request.POST.get('email')
                user.password = request.POST.get('pass')
                user.phone = request.POST.get('phone')
                user.address = request.POST.get('address')
                user.save()
                messages.success(request, "registered successfully")
                return redirect('/client_login.html')
        return render(request, "register.html")

def login(request):
    if "user" in request.session:
        messages.success(request, 'already logged in')
        return redirect('/client.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')
            print(1)
            try:
                user = Client.objects.get(username=username)
                if user.password != password:
                    print(12)
                    messages.success(request, 'password is wrong')
                    return redirect('/user_login.html')
                print(123)
                request.session['client'] = user.username
                return redirect('/client.html')
            except Client.DoesNotExist:
                print(133)
                messages.success(request, 'username does not exist')
                return redirect('/client_login.html')
        return render(request, "login.html", {'name': 'client'})

def page(request):
    if 'client' in request.session:
        return render(request,'client.html')
    else:
        return redirect('/client_login.html')


def logout(request):
    if 'client' in request.session:
        request.session.pop('client',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session loggedout')
        return redirect('/client_login.html')
