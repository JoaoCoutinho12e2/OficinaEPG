from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from dashboard.models import Servico
from dashboard.forms import ContactForm


def landing_page(request):
    return render(request, 'core/landing.html')


def servicos_list(request):
    """Public page displaying all available services"""
    servicos = Servico.objects.all().order_by('nome')

    # Add pagination
    paginator = Paginator(servicos, 6)  # Show 6 services per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_servicos': servicos.count(),
    }
    return render(request, 'core/servicos_list.html', context)


def login_view(request):
    """Login view with custom template"""
    if request.user.is_authenticated:
        return redirect('dashboard_home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')

            # Redirect to dashboard if staff, otherwise to services
            if user.is_staff:
                return redirect('dashboard_home')
            else:
                return redirect('servicos_list')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    """Logout view"""
    if request.user.is_authenticated:
        username = request.user.username
        auth_logout(request)
        messages.success(request, f'Até logo, {username}!')

    return redirect('landing')


def contact_view(request):
    """Contact form view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to database
            mensagem = form.save()

            # Send email notification
            try:
                assunto = mensagem.assunto or 'Sem assunto'
                subject = f"Nova mensagem de contacto: {assunto}"
                message = f"""
Nova mensagem recebida através do formulário de contacto:

Nome: {mensagem.nome}
Email: {mensagem.email}
Assunto: {mensagem.assunto or 'Sem assunto'}
Data: {mensagem.recebido_em.strftime('%d/%m/%Y às %H:%M')}

Mensagem:
{mensagem.mensagem}

---
Esta mensagem foi enviada automaticamente pelo sistema da Oficina EPG.
                """.strip()

                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,  # Don't break if email fails
                )
            except Exception as e:
                # Log the error but don't break the user experience
                print(f"Email sending failed: {e}")

            messages.success(
                request,
                'Mensagem enviada com sucesso! '
                'Entraremos em contacto consigo brevemente.'
            )
            return redirect('contact')
        else:
            messages.error(
                request,
                'Erro ao enviar mensagem. '
                'Por favor, verifique os dados e tente novamente.'
            )
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})
