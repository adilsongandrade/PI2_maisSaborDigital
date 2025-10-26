from django.urls import path
from . import views
#from .views import login_view, home_view, ficha_view

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('ficha/', views.ficha_view, name='ficha'),
    # NOVO: Rota para a simulação
    path('simular-preco/', views.simular_preco_view, name='simular_preco'),
]