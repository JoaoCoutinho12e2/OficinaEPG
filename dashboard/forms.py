# dashboard/forms.py
from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao', 'imagem_url', 'preco']

    def clean_preco(self):
        preco = self.cleaned_data['preco']
        if preco < 0:
            raise forms.ValidationError("O preço não pode ser negativo.")
        return preco

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if not nome:
            raise forms.ValidationError("O nome é obrigatório.")
        return nome