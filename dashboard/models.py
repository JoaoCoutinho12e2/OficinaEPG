# models.py

from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User model without role dependency"""
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Servico(models.Model):
    """Service model"""
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    imagem_url = models.TextField(blank=True, null=True)
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00")
    )

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    """Appointment model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=20, blank=True, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.RESTRICT)
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome_cliente} - {self.servico.nome}"


class MensagemContacto(models.Model):
    """Contact Message model"""
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=150, blank=True, null=True)
    mensagem = models.TextField()
    recebido_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.assunto}"