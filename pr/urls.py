from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('', views.index, name='index'),
    # Каталог
    path('catalog/', views.catalog_main, name='catalog_main'),
    path('catalog/list/', views.catalog_list, name='catalog_list'),
    path('catalog/add/', views.catalog_add, name='catalog_add'),
    path('catalog/<int:product_id>/', views.catalog_detail, name='catalog_detail'),

    # Категории и теги
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/<int:tag_id>/', views.products_by_tag, name='products_by_tag'),

    # Прочее
    path('feedback/', views.feedback, name='feedback'),
    path('api-info/', views.api_page, name='api_page'),  

   

    # Подключение приложений
    path('api/', include('api_shop.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
