from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import DroneViewSet, MedicationViewSet, ShippingViewSet

router = DefaultRouter()
router.register('drones', DroneViewSet, basename='drones')
router.register('medication', MedicationViewSet, basename='medication')
router.register('shipping', ShippingViewSet, basename='shipping')

urlpatterns = router.urls
