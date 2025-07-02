# core/views.py

from django.shortcuts import render

def landing_page(request):
    return render(request, 'core/landing.html')

def login_view(request):
    return render(request, 'core/login.html')

def register_view(request):
    return render(request, 'core/register.html')
