from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import CreateUserForm, AppointmentForm, ContactForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
# @login_required(login_url='login') 
def home(request):
    return render(request, 'index.html', {})

@login_required(login_url='login') 
def contactus(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            return render(request, 'contact.html', {'submitted':submitted})
    else:
        form = ContactForm()        
    return render(request, 'contact.html', {'form':form, 'submitted':submitted})

def errorpage(request):
    return render(request, '404.html', {})

from .models import Comment
def blog_details(request):
    post = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog-single.html', { 'post':post})
    else:
        form = CommentForm()        
    return render(request, 'blog-single.html', {'form':form, 'post':post})

def portfolio_details(request):
    return render(request, 'portfolio-details.html', {})

from .models import Doctor
def doctors_details(request):
    post = Doctor.objects.all()
    return render(request, 'doctors.html', {'post': post})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Either username or password is incorrect')
        return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('home')

def signup_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Hey, {user} Your account has been created successfully!')
                return redirect('login')
        return render(request, 'signup.html', {'form': form})
    
@login_required(login_url='login') 
def appointment(request):
    submitted = False
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            return render(request, 'appointment.html', {'submitted':submitted})
    else:
        form = AppointmentForm()
        
    return render(request, 'appointment.html', {'form':form, 'submitted':submitted})

def handler404(request, exception):
    return HttpResponse("<h1>NOT FOUND</h1>", status = 404)