# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product
from django.http import JsonResponse

def home(request):
    return render(request, 'core/home.html')

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
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total_product_price = product.price * quantity
        products.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_product_price,
        })
        total_price += total_product_price

    if coupon == "DESC10":
        discount = total_price * 0.1

    context = {
        'products': products,
        'total_price': total_price,
        'discount': discount,
        'final_price': total_price - discount,
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
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']
        product = Product(name=name, description=description, price=price, image=image)
        product.save()
        return redirect('pedido')
    return redirect('pedido')

@login_required
def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        product.image.delete()
        product.delete()
        return redirect('list_pedidos')
    return redirect('list_pedidos')

def list_pedidos(request):
    products = Product.objects.all()
    return render(request, 'core/list_pedidos.html', {'products': products})

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
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})

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
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})

def clear_cart(request):
    request.session['cart'] = {}
    #request.session.save()
    return redirect('list_pedidos')

def apply_coupon(request):
    if request.method == 'POST':
        coupon = request.POST.get('coupon')
        request.session['coupon'] = coupon
    return redirect('list_pedidos')
