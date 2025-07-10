# admin.py
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import User, Servico, Agendamento, MensagemContacto

# Customize admin site header
admin.site.site_header = "Oficina EPG - Administração"
admin.site.site_title = "Oficina EPG Admin"
admin.site.index_title = "Painel de Administração"

# Enhanced Service admin
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_formatado', 'tem_imagem', 'tem_descricao', 'acoes')
    search_fields = ('nome', 'descricao')
    list_filter = ('preco',)
    ordering = ('nome',)

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'preco')
        }),
        ('Detalhes', {
            'fields': ('descricao', 'imagem_url'),
            'classes': ('collapse',)
        }),
    )

    def preco_formatado(self, obj):
        return f"€{obj.preco:.2f}"
    preco_formatado.short_description = "Preço"
    preco_formatado.admin_order_field = "preco"

    def tem_imagem(self, obj):
        if obj.imagem_url:
            return format_html(
                '<span style="color: green;">✓ Sim</span>'
            )
        return format_html(
            '<span style="color: red;">✗ Não</span>'
        )
    tem_imagem.short_description = "Imagem"

    def tem_descricao(self, obj):
        if obj.descricao:
            return format_html(
                '<span style="color: green;">✓ Sim</span>'
            )
        return format_html(
            '<span style="color: red;">✗ Não</span>'
        )
    tem_descricao.short_description = "Descrição"

    def acoes(self, obj):
        return format_html(
            '<a class="button" href="{}">Editar</a>',
            reverse('admin:dashboard_servico_change', args=[obj.pk])
        )
    acoes.short_description = "Ações"

# Enhanced Appointment admin
@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'servico', 'data_hora_formatada', 'preco_servico', 'contacto')
    search_fields = ('nome_cliente', 'email_cliente', 'telefone_cliente')
    list_filter = ('data_hora', 'servico', 'user')
    date_hierarchy = 'data_hora'
    ordering = ('-data_hora',)

    fieldsets = (
        ('Cliente', {
            'fields': ('nome_cliente', 'email_cliente', 'telefone_cliente')
        }),
        ('Agendamento', {
            'fields': ('user', 'servico', 'data_hora')
        }),
        ('Observações', {
            'fields': ('observacoes',),
            'classes': ('collapse',)
        }),
    )

    def data_hora_formatada(self, obj):
        return obj.data_hora.strftime("%d/%m/%Y às %H:%M")
    data_hora_formatada.short_description = "Data e Hora"
    data_hora_formatada.admin_order_field = "data_hora"

    def preco_servico(self, obj):
        return f"€{obj.servico.preco:.2f}"
    preco_servico.short_description = "Preço"

    def contacto(self, obj):
        return format_html(
            '<a href="mailto:{}">{}</a>',
            obj.email_cliente,
            obj.email_cliente
        )
    contacto.short_description = "Email"

# Enhanced User admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'is_staff',
        'is_superuser',
        'is_active',
        'criado_em_formatado'
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'criado_em')
    ordering = ('-criado_em',)

    fieldsets = (
        ('Informações de Login', {
            'fields': ('username', 'password')
        }),
        ('Informações Pessoais', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )

    def criado_em_formatado(self, obj):
        return obj.criado_em.strftime("%d/%m/%Y às %H:%M")
    criado_em_formatado.short_description = "Registado em"
    criado_em_formatado.admin_order_field = "criado_em"


@admin.register(MensagemContacto)
class MensagemContactoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'recebido_em_formatado')
    search_fields = ('nome', 'email', 'assunto', 'mensagem')
    list_filter = ('recebido_em',)
    date_hierarchy = 'recebido_em'
    ordering = ('-recebido_em',)
    readonly_fields = ('recebido_em',)

    fieldsets = (
        ('Remetente', {
            'fields': ('nome', 'email')
        }),
        ('Mensagem', {
            'fields': ('assunto', 'mensagem')
        }),
        ('Informações do Sistema', {
            'fields': ('recebido_em',),
            'classes': ('collapse',)
        }),
    )

    def recebido_em_formatado(self, obj):
        return obj.recebido_em.strftime("%d/%m/%Y às %H:%M")
    recebido_em_formatado.short_description = "Recebido em"
    recebido_em_formatado.admin_order_field = "recebido_em"