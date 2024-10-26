from django.shortcuts import render,redirect,Http404,HttpResponse
from django.contrib import messages
import os
from django.conf import settings
from user.models import *
from django.core.mail import send_mail
from .models import *
# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def contact_save(request):
    con=Contact()
    con.name=request.POST.get('name')
    con.subject=request.POST.get('subject')
    con.msg=request.POST.get('message')
    con.email=request.POST.get('email')
    con.save()
    send_mail('alazea','welcome to alazea , your request accepted successfully.',settings.DEFAULT_FROM_EMAIL, [request.POST.get('email')])
    messages.success(request,'thank you for contacting us')
    return redirect('/')

def admin_login(request):
    if request.method=='POST':
        email=str(request.POST.get('username'))
        pas=str(request.POST.get('pass'))
        if (email == 'admin') & (pas == '1234'):
            request.session['admin']='admin'
            return redirect('/admin.html')
    return render(request,'login.html',{'name':'admin'})

def admin_page(request):
    if "admin" in request.session:
        return render(request,'admin.html')
    else:
        return redirect('/admin_login.html')

def admin_logout(request):
    if 'admin' in request.session:
        request.session.pop('admin')
        messages.success(request,'logged out')
        return redirect('/')
    else:
        return redirect('/admin_login.html')
