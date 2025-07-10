from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from dashboard.models import Servico
from decimal import Decimal


class Command(BaseCommand):
    help = 'Setup initial data for the application'

    def handle(self, *args, **options):
        self.stdout.write('Setting up initial data...')

        # Create admin user
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_user(
                username='admin',
                email='admin@oficinaepg.com',
                password='admin123',
                is_staff=True,
                is_superuser=True
            )
            self.stdout.write(f'Created admin user: {admin_user.username}')

        # Create sample services
        sample_services = [
            {
                'nome': 'Mudança de Óleo',
                'descricao': 'Mudança completa de óleo do motor',
                'preco': Decimal('45.00'),
                'imagem_url': 'https://example.com/mudanca-oleo.jpg'
            },
            {
                'nome': 'Revisão Geral',
                'descricao': 'Revisão completa do veículo',
                'preco': Decimal('120.00'),
                'imagem_url': 'https://example.com/revisao-geral.jpg'
            },
            {
                'nome': 'Troca de Pneus',
                'descricao': 'Montagem e balanceamento de pneus novos',
                'preco': Decimal('25.00'),
                'imagem_url': 'https://example.com/troca-pneus.jpg'
            },
            {
                'nome': 'Diagnóstico Eletrónico',
                'descricao': 'Diagnóstico dos sistemas eletrónicos',
                'preco': Decimal('35.00'),
                'imagem_url': 'https://example.com/diagnostico.jpg'
            }
        ]

        for service_data in sample_services:
            servico, created = Servico.objects.get_or_create(
                nome=service_data['nome'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'Created service: {servico.nome}')

        self.stdout.write(
            self.style.SUCCESS('Successfully set up initial data!')
        )
        self.stdout.write(
            'Admin credentials: username=admin, password=admin123'
        )
