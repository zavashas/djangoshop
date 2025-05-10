from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from app.models import Product, Category, Tag, Order, OrderItem
from app.forms import ProductForm, CategoryForm, OrderCreateForm, CustomUserCreationForm, CustomAuthenticationForm
from cart.cart import Cart
import uuid
from django.core.mail import send_mail
# Create your views here.
@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.number = str(uuid.uuid4())[:8].upper()
            order.user = request.user  
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    discount=0
                )

            cart.clear()

            send_mail(
                subject=f'Заказ №{order.number} оформлен',
                message=(
                    f'Здравствуйте, {order.customer_name}!\n\n'
                    f'Спасибо за ваш заказ №{order.number}.\n'
                    f'Мы свяжемся с вами по номеру {order.phone}.\n\n'
                    f'С уважением,\nMebelHome'
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[order.email],
                fail_silently=False
            )

            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form': form, 'cart': cart})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})


@staff_member_required(login_url='login')
def admin_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders/admin_orders.html', {'orders': orders})


