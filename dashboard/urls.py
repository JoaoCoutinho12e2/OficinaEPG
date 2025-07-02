from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('precos/', views.dashboard_precos, name='dashboard_precos'),
    path('servicos/', views.dashboard_servicos, name='dashboard_servicos'),
]
