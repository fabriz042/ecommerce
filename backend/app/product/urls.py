from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet, CategoryViewSet, StatusViewSet, BrandViewSet,
    SeriesViewSet, CharacterViewSet, TagViewSet, SportViewSet
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'statuses', StatusViewSet, basename='status')
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'series', SeriesViewSet, basename='series')
router.register(r'characters', CharacterViewSet, basename='character')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'sports', SportViewSet, basename='sport')

urlpatterns = [
    path('api/', include(router.urls)),
]
