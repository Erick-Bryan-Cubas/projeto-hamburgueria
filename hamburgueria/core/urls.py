# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pedido/', views.pedido, name='pedido'),
    path('agradecimento/', views.agradecimento, name='agradecimento'),
]
