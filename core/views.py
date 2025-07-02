from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login

def landing_page(request):
    return render(request, 'core/landing.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard_home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'core/login.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard_home')
    else:
        form = UserCreationForm()
    
    return render(request, 'core/register.html', {'form': form})