from rest_framework import routers
from order.api import FlavorViewSet, SizeViewSet, PizzaViewSet, CustomerViewSet, OrderStatusViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('api/flavors', FlavorViewSet, 'flavors')
router.register('api/sizes', SizeViewSet, 'sizes')
router.register('api/pizzas', PizzaViewSet, 'pizzas')
router.register('api/customers', CustomerViewSet, 'customers')
router.register('api/order/status', OrderStatusViewSet, 'order_status')
router.register('api/order', OrderViewSet, 'order')

urlpatterns = router.urls
