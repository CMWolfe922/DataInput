from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet, CustomerViewSet, ContactViewSet, LocationViewSet
from .views import PickupViewSet, DeliveryViewSet, DriverViewSet

router = routers.DefaultRouter()

router.register(r'order', OrderViewSet)
router.register(r'customer',CustomerViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'location', LocationViewSet)
router.register(r'pickup', PickupViewSet)
router.register(r'delivery', DeliveryViewSet)
router.register(r'driver', DriverViewSet)

urlpatterns = [
    path('', include(router.urls)),
]