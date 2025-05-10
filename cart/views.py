import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from app.models import Product
from .cart import Cart

# Страница корзины
@login_required(login_url='login')
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart, 'now': timezone.now()})

# Добавление товара в корзину
@require_POST
@login_required(login_url='login')
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart')

# Удаление товара из корзины
@login_required(login_url='login')
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart')

# Обновление количества товара в корзине (AJAX)
@require_POST
@login_required(login_url='login')
def cart_update(request):
    data = json.loads(request.body)
    product_id = str(data['product_id'])
    quantity = int(data['quantity'])

    cart = Cart(request)
    cart.update(product_id, quantity)

    product = get_object_or_404(Product, id=product_id)
    item_total = quantity * float(product.price)
    cart_total = cart.get_total_price()

    return JsonResponse({
        'item_total': f"{item_total:.2f}",
        'cart_total': f"{cart_total:.2f}"
    })
