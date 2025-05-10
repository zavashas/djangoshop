from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from cart.cart import Cart


# Главная страница
def index(request):
    return render(request, 'app/index.html', {'now': timezone.now()})



def catalog_main(request):
    products = Product.objects.filter(is_deleted=False)
    cart = Cart(request)
    # Преобразуем ключи (строки) в int для сравнения с product.id
    cart_product_ids = [int(pid) for pid in cart.cart.keys()]
    
    return render(request, 'app/catalog/main.html', {
        'products': products,
        'cart_product_ids': cart_product_ids,
        'now': timezone.now()
    })


# Список всех товаров
def catalog_list(request):
    products = Product.objects.filter(is_deleted=False)
    return render(request, 'app/catalog/list.html', {'products': products, 'now': timezone.now()})

# Добавление товара
@staff_member_required(login_url='login')
def catalog_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog_main')
    else:
        form = ProductForm()
    return render(request, 'app/catalog/add.html', {'form': form, 'now': timezone.now()})

# Просмотр товара
def catalog_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'app/catalog/detail.html', {'product': product, 'now': timezone.now()})

# Редактирование товара
@staff_member_required(login_url='login')
def catalog_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalog_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'app/catalog/edit.html', {'form': form, 'now': timezone.now()})

# Обратная связь
def feedback(request):
    return render(request, 'app/feedback.html', {'now': timezone.now()})

# Страница API
def api_page(request):
    return render(request, 'app/api.html', {'now': timezone.now()})  




# Список категорий
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'app/categories/list.html', {'categories': categories, 'now': timezone.now()})

# Добавление категории
@staff_member_required(login_url='login')
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'app/categories/add.html', {'form': form, 'now': timezone.now()})

# Товары по категории
def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, is_deleted=False)
    return render(request, 'app/catalog/list_by_category.html', {'category': category, 'products': products, 'now': timezone.now()})

# Товары по тегу
def products_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    products = Product.objects.filter(tags=tag, is_deleted=False)
    return render(request, 'app/catalog/list_by_tag.html', {'tag': tag, 'products': products, 'now': timezone.now()})

# Список тегов
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'app/tags/list.html', {'tags': tags, 'now': timezone.now()})


