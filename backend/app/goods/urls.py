from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BagViewSet, AirgearViewSet, OilViewSet, TrophyViewSet, GloveViewSet, AttributeViewSet
)

router = DefaultRouter()
router.register(r'bags', BagViewSet, basename='bag')
router.register(r'airgear', AirgearViewSet, basename='airgear')
router.register(r'oil', OilViewSet, basename='oil')
router.register(r'trophy', TrophyViewSet, basename='trophy')
router.register(r'glove', GloveViewSet, basename='glove')
router.register(r'attribute', AttributeViewSet, basename='attribute')

urlpatterns = [
    path('api/', include(router.urls)),
]
