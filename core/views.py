from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login

def landing_page(request):
    return render(request, 'core/landing.html')
