from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
     # Заказы
    path('order/create/', order_create, name='order_create'),
    path('my-orders/', my_orders, name='my_orders'),
    path('orders/', admin_orders, name='admin_orders'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
