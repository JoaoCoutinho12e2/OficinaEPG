# dashboard/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_home(request):
    return render(request, 'dashboard/home.html')

@login_required
def dashboard_precos(request):
    return render(request, 'dashboard/precos.html')

@login_required
def dashboard_servicos(request):
    return render(request, 'dashboard/servicos.html')
