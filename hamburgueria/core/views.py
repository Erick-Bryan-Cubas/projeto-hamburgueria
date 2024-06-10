# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', {'products': products})

def pedido(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'core/pedido.html')

def agradecimento(request):
    cart = request.session.get('cart', {})
    coupon = request.session.get('coupon', '')
    discount = 0
    products = []
    total_price = 0
    total_preparation_time = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total_product_price = product.price * quantity

        if product.discount:
            total_product_price *= (1 - product.discount / 100)

        products.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_product_price,
        })
        total_price += total_product_price
        total_preparation_time += product.preparation_time * quantity

    if coupon == "DESC10":
        discount = total_price * 0.1

    if total_price >= 80:
        shipping_cost = 0
    else:
        shipping_cost = 15

    final_price = total_price - discount + shipping_cost

    context = {
        'products': products,
        'total_price': total_price,
        'discount': discount,
        'shipping_cost': shipping_cost,
        'final_price': final_price,
        'preparation_time': total_preparation_time,
    }
    return render(request, 'core/agradecimento.html', context)

def register(request):
    return render(request, 'core/register.html')

def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        return redirect('login')
    return redirect('register')

@login_required
def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST.get('description', '')
        price = request.POST['price']
        image = request.FILES['image']
        preparation_time = request.POST['preparation_time']
        discount = request.POST.get('discount', None)
        if discount:
            discount = float(discount)
        product = Product(name=name, description=description, price=price, image=image, preparation_time=preparation_time, discount=discount)
        product.save()
        return redirect('pedido')
    return redirect('pedido')

@login_required
def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return redirect('list_pedidos')
    return redirect('list_pedidos')

def list_pedidos(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    coupon = request.session.get('coupon', '')
    discount = 0
    total_price = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        product_total = product.price * quantity
        if product.discount:
            product_total *= (1 - product.discount / 100)
        total_price += product_total

    if coupon == "DESC10":
        discount = total_price * 0.1

    if total_price >= 80:
        shipping_cost = 0
    else:
        shipping_cost = 15

    final_price = total_price - discount + shipping_cost

    return render(request, 'core/list_pedidos.html', {
        'products': products,
        'total_price': total_price,
        'discount': discount,
        'shipping_cost': shipping_cost,
        'final_price': final_price,
    })

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        request.session['cart'] = cart
    return redirect('list_pedidos')

def remove_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] -= quantity
            if cart[product_id] <= 0:
                del cart[product_id]
        request.session['cart'] = cart
    return redirect('list_pedidos')

def clear_cart(request):
    request.session['cart'] = {}
    return redirect('list_pedidos')

def apply_coupon(request):
    if request.method == 'POST':
        coupon = request.POST.get('coupon')
        request.session['coupon'] = coupon
    return redirect('list_pedidos')
