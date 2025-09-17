from rest_framework import viewsets
from .models import (Bag, Airgear, Oil, Trophy, Glove, Attribute)
from .serializer import (
    BagSerializer, BagDetailSerializer, 
    AirgearSerializer, AirgearDetailSerializer, 
    OilSerializer, OilDetailSerializer, 
    TrophySerializer, TrophyDetailSerializer, 
    GloveSerializer, GloveDetailSerializer, 
    AttributeSerializer, AttributeDetailSerializer
)
from .permissions import GoodsPermission
class BagViewSet(viewsets.ModelViewSet):
    permission_classes = [GoodsPermission]
    serializer_class = BagSerializer
    serializer_map = {
        "list": BagDetailSerializer,
        "retrieve": BagDetailSerializer,
    }
    queryset = Bag.objects.all()
    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)
class AirgearViewSet(viewsets.ModelViewSet):
    permission_classes = [GoodsPermission]
    serializer_class = AirgearSerializer
    serializer_map = {
        "list": AirgearDetailSerializer,
        "retrieve": AirgearDetailSerializer,
    }
    queryset = Airgear.objects.all()
    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)
class OilViewSet(viewsets.ModelViewSet):
    permission_classes = [GoodsPermission]
    serializer_class = OilSerializer
    serializer_map = {
        "list": OilDetailSerializer,
        "retrieve": OilDetailSerializer,
    }
    queryset = Oil.objects.all()
    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)
class TrophyViewSet(viewsets.ModelViewSet):
    permission_classes = [GoodsPermission]
    serializer_class = TrophySerializer
    serializer_map = {
        "list": TrophyDetailSerializer,
        "retrieve": TrophyDetailSerializer,
    }
    queryset = Trophy.objects.all()
    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)
class GloveViewSet(viewsets.ModelViewSet):
    permission_classes = [GoodsPermission]
    serializer_class = GloveSerializer
    serializer_map = {
        "list": GloveDetailSerializer,
        "retrieve": GloveDetailSerializer,
    }
    queryset = Glove.objects.all()
    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)
class AttributeViewSet(viewsets.ModelViewSet):
    permission_classes = [GoodsPermission]
    serializer_class = AttributeSerializer
    serializer_map = {
        "list": AttributeDetailSerializer,
        "retrieve": AttributeDetailSerializer,
    }
    queryset = Attribute.objects.all()
    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)
