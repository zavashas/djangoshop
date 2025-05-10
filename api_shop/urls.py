from rest_framework import routers
from django.urls import path
from .views import (
    ProductViewSet,
    CategoryViewSet,
    TagViewSet,
    OrderViewSet,
    OrderItemViewSet,
)

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = []

urlpatterns += router.urls
