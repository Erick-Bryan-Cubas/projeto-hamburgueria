# core/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('pedido/', views.pedido, name='pedido'),
    path('agradecimento/', views.agradecimento, name='agradecimento'),
    path('register/', views.register, name='register'),
    path('users/', views.create_user, name='create_user'),
    path('pedidos/', views.create_product, name='create_product'),
    path('list_pedidos/', views.list_pedidos, name='list_pedidos'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('apply_coupon/', views.apply_coupon, name='apply_coupon'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
