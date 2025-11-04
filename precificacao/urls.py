# PI2_maisSaborDigital/precificacao/urls.py (Versão Corrigida)
from django.urls import path
from . import views

urlpatterns = [
    # Usa a sub-rota 'aliquota/' para ser mais explícito.
    # A URL completa será: /api/precificacao/aliquota/
    path('aliquota/', views.calcular_aliquota_proxy, name='simples_nacional_aliquota_proxy'), 
]