# core/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def pedido(request):
    return render(request, 'core/pedido.html')

def agradecimento(request):
    return render(request, 'core/agradecimento.html')
