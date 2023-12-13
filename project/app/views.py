from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import reg_form, login_form
from .models import UserModel


def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        register = UserModel(name=name, email=email, password=password)
        register.save()
        return redirect('login')
    else:
        form = reg_form()
    return render(request, 'register/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if email == 'User1@gmail.com' and password == '12345678':
                return redirect('profile')
            else:
                return redirect('error')
    else:
        form = login_form()
    return render(request, 'register/login.html', {'form': form})

def error_view(request):
    return render(request, 'register/error.html')

def profile_view(request):
    return render(request, 'register/profile.html')