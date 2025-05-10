from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app.models import Product, Category, Tag, Order, OrderItem

from .serializers import (
    ProductSerializer,
    CategorySerializer,
    TagSerializer,
    OrderSerializer,
    OrderItemSerializer
)
from .permissions import CustomPermissions, PaginationPage  


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage  

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Admin').exists():
            return Order.objects.all()
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
