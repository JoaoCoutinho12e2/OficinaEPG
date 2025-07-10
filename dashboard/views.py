# dashboard/views.py
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import User, Servico, Agendamento, MensagemContacto
from django.contrib import messages
from .forms import ServicoForm


@login_required
@staff_member_required
def dashboard_home(request):
    """Dashboard home view - requires staff access"""
    # Paginated users
    users = User.objects.all().order_by('id')
    paginator = Paginator(users, 10)  # 10 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Additional dashboard data
    total_users = User.objects.count()
    total_servicos = Servico.objects.count()
    total_mensagens = MensagemContacto.objects.count()
    recent_agendamentos = Agendamento.objects.order_by('-data_hora')[:5]
    recent_mensagens = MensagemContacto.objects.order_by('-recebido_em')[:5]

    context = {
        'page_obj': page_obj,
        'total_users': total_users,
        'total_servicos': total_servicos,
        'total_mensagens': total_mensagens,
        'recent_agendamentos': recent_agendamentos,
        'recent_mensagens': recent_mensagens,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
@staff_member_required
def dashboard_precos(request):
    """Dashboard prices view"""
    servicos = Servico.objects.all().order_by('nome')

    context = {
        'servicos': servicos,
        'total_servicos': servicos.count(),
    }
    return render(request, 'dashboard/precos.html', context)



@login_required
@staff_member_required
def dashboard_servicos(request):
    """Dashboard services management view (CRUD)"""
    servicos = Servico.objects.all().order_by('nome')
    context = {
        'servicos': servicos,
        'total_servicos': servicos.count(),
    }
    return render(request, 'dashboard/precos.html', context)

@login_required
@staff_member_required
def edit_servico(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço atualizado com sucesso!')
            return redirect('dashboard_servicos')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'dashboard/add_servico.html', {'form': form, 'edit': True})

@login_required
@staff_member_required
def delete_servico(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    if request.method == 'POST':
        servico.delete()
        messages.success(request, 'Serviço excluído com sucesso!')
        return redirect('dashboard_servicos')
    return render(request, 'dashboard/delete_confirm.html', {'servico': servico})


def servicos_list(request):
    """Public services list view"""
    servicos = Servico.objects.all()
    return render(request, 'servicos_list.html', {'servicos': servicos})


@login_required
@staff_member_required
def add_servico(request):
    """Add new service view - requires staff access"""
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço adicionado com sucesso!')
            return redirect('dashboard_home')
    else:
        form = ServicoForm()
    return render(request, 'dashboard/add_servico.html', {'form': form})


@login_required
@staff_member_required
def dashboard_mensagens(request):
    """Dashboard contact messages view"""
    mensagens = MensagemContacto.objects.all().order_by('-recebido_em')

    # Add pagination
    paginator = Paginator(mensagens, 10)  # 10 messages per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_mensagens': mensagens.count(),
    }
    return render(request, 'dashboard/mensagens.html', context)