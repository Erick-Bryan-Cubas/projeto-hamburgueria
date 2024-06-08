# hamburgueria/core/routing.py
from django.urls import path
from .consumers import CartConsumer

websocket_urlpatterns = [
    path('ws/cart/', CartConsumer.as_asgi()),
]
