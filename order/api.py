from order.models import Flavor, Size, Pizza, Customer, OrderStatus, Order
from rest_framework import viewsets, permissions
from .serializers import FlavorSerializer, SizeSerializer, PizzaSerializer, CustomerSerializer, OrderStatusSerializer, \
    OrderSerializer


class FlavorViewSet(viewsets.ModelViewSet):
    queryset = Flavor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    http_method_names = ['get']
    serializer_class = FlavorSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    http_method_names = ['get']
    serializer_class = SizeSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PizzaSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    http_method_names = ['get']
    serializer_class = OrderStatusSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer
    filter_fields = ('id', 'status__id', 'customer__id', )

