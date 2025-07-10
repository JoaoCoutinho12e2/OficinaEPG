# dashboard/forms.py
from django import forms
from django.core.validators import URLValidator
from .models import Servico, MensagemContacto


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao', 'imagem_url', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Mudança de óleo',
                'maxlength': 100
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descreva detalhadamente o serviço oferecido...',
                'rows': 4
            }),
            'imagem_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://exemplo.com/imagem.jpg'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            })
        }
        labels = {
            'nome': 'Nome do Serviço',
            'descricao': 'Descrição',
            'imagem_url': 'URL da Imagem',
            'preco': 'Preço (€)'
        }
        help_texts = {
            'nome': 'Digite o nome do serviço (máximo 100 caracteres)',
            'descricao': 'Descrição detalhada do serviço (opcional)',
            'imagem_url': 'Link para imagem do serviço (opcional)',
            'preco': 'Preço do serviço em euros'
        }

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco is not None and preco < 0:
            raise forms.ValidationError("O preço não pode ser negativo.")
        if preco is not None and preco > 9999.99:
            raise forms.ValidationError("O preço não pode exceder €9999.99.")
        return preco

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            raise forms.ValidationError("O nome é obrigatório.")
        if len(nome.strip()) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return nome.strip()

    def clean_imagem_url(self):
        imagem_url = self.cleaned_data.get('imagem_url')
        if imagem_url:
            # Validate URL format
            validator = URLValidator()
            try:
                validator(imagem_url)
            except forms.ValidationError:
                raise forms.ValidationError("Por favor, insira uma URL válida.")

            # Check if URL ends with image extension
            valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
            if not any(imagem_url.lower().endswith(ext) for ext in valid_extensions):
                raise forms.ValidationError(
                    "A URL deve apontar para uma imagem válida (.jpg, .jpeg, .png, .gif, .webp)."
                )
        return imagem_url

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if descricao and len(descricao.strip()) > 1000:
            raise forms.ValidationError(
                "A descrição não pode exceder 1000 caracteres."
            )
        return descricao.strip() if descricao else descricao


class ContactForm(forms.ModelForm):
    """Contact form with validation"""

    class Meta:
        model = MensagemContacto
        fields = ['nome', 'email', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'O seu nome completo',
                'maxlength': 100
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'o.seu.email@exemplo.com'
            }),
            'assunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Assunto da mensagem',
                'maxlength': 150
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escreva a sua mensagem aqui...',
                'rows': 5
            })
        }
        labels = {
            'nome': 'Nome Completo',
            'email': 'Email',
            'assunto': 'Assunto',
            'mensagem': 'Mensagem'
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            raise forms.ValidationError("O nome é obrigatório.")
        if len(nome.strip()) < 2:
            raise forms.ValidationError(
                "O nome deve ter pelo menos 2 caracteres."
            )
        if len(nome.strip()) > 100:
            raise forms.ValidationError(
                "O nome não pode exceder 100 caracteres."
            )
        return nome.strip()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O email é obrigatório.")
        return email.lower().strip()

    def clean_assunto(self):
        assunto = self.cleaned_data.get('assunto')
        if assunto and len(assunto.strip()) > 150:
            raise forms.ValidationError(
                "O assunto não pode exceder 150 caracteres."
            )
        return assunto.strip() if assunto else assunto

    def clean_mensagem(self):
        mensagem = self.cleaned_data.get('mensagem')
        if not mensagem:
            raise forms.ValidationError("A mensagem é obrigatória.")
        if len(mensagem.strip()) < 10:
            raise forms.ValidationError(
                "A mensagem deve ter pelo menos 10 caracteres."
            )
        if len(mensagem.strip()) > 2000:
            raise forms.ValidationError(
                "A mensagem não pode exceder 2000 caracteres."
            )
        return mensagem.strip()