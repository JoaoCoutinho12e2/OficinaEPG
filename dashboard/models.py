# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Role model
class Role(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

# Custom User model
class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.RESTRICT)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

# Service model
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    imagem_url = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome

# Appointment model
class Agendamento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=20, blank=True, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.RESTRICT)
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome_cliente} - {self.servico.nome}"

# Contact Message model
class MensagemContacto(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=150, blank=True, null=True)
    mensagem = models.TextField()
    recebido_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.assunto}"