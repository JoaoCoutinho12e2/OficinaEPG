from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('servicos/', views.servicos_list, name='servicos_list'),
    path('contacto/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
