from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductsView

router = DefaultRouter()

router.register('api/products', ProductsView, basename='product')

urlpatterns = router.urls
