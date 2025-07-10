from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('precos/', views.dashboard_precos, name='dashboard_precos'),
    path('servicos/', views.dashboard_servicos, name='dashboard_servicos'),
    path('servicos/add/', views.add_servico, name='add_servico'),
    path('servicos/edit/<int:servico_id>/', views.edit_servico, name='edit_servico'),
    path('servicos/delete/<int:servico_id>/', views.delete_servico, name='delete_servico'),
    path('mensagens/', views.dashboard_mensagens, name='dashboard_mensagens'),
]
