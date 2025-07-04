# dashboard/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import User, Servico, Agendamento
from django.contrib import messages
from .forms import ServicoForm

@login_required
def dashboard_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not hasattr(request.user, 'role') or request.user.role.nome != 'admin':
        return redirect('servicos_list')

    # Paginated users
    users = User.objects.all().order_by('id')
    paginator = Paginator(users, 10)  # 10 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Additional dashboard data
    total_users = User.objects.count()
    total_servicos = Servico.objects.count()
    recent_agendamentos = Agendamento.objects.order_by('-data_hora')[:5]

    context = {
        'page_obj': page_obj,
        'total_users': total_users,
        'total_servicos': total_servicos,
        'recent_agendamentos': recent_agendamentos,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def dashboard_precos(request):
    return render(request, 'dashboard/precos.html')

@login_required
def dashboard_servicos(request):
    return render(request, 'dashboard/servicos.html')

@login_required
def servicos_list(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos_list.html', {'servicos': servicos})

@login_required
def add_servico(request):
    if not request.user.is_authenticated or request.user.role.nome != 'admin':
        return redirect('login')

    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço adicionado com sucesso!')
            return redirect('dashboard_home')
    else:
        form = ServicoForm()
    return render(request, 'dashboard/add_servico.html', {'form': form})