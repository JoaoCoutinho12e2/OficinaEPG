# admin.py
from django.contrib import admin
from .models import Role, User, Servico, Agendamento, MensagemContacto

# Customize Service admin
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fields = ('nome',)
    list_filter = ('preco',)

# Customize Appointment admin
@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'servico', 'data_hora')
    search_fields = ('nome_cliente', 'email_cliente')
    list_filter = ('data_hora', 'servico')
    date_hierarchy = 'data_hora'

# Register other models with default settings
admin.site.register(Role)
admin.site.register(User)
admin.site.register(MensagemContacto)