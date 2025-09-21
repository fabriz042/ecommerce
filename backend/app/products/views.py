from rest_framework import viewsets
from .schema_docs import product_docs

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import ProductFilter

from .models import (Product, Category, Status, Brand, Series, Character, Tag, Sport)
from .serializer import (
    ProductSerializer, ProductDetailSerializer,
    CategorySerializer, CategoryDetailSerializer,
    StatusSerializer, StatusDetailSerializer,
    BrandSerializer, BrandDetailSerializer,
    SeriesSerializer, SeriesDetailSerializer,
    CharacterSerializer, CharacterDetailSerializer,
    TagSerializer, TagDetailSerializer,
    SportSerializer, SportDetailSerializer
)
from .permissions import (ProductPermission)
from utils.CustomPagination import CustomPagination

@product_docs
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = ProductSerializer
    serializer_map = {
        "list": ProductDetailSerializer,
        "retrieve": ProductDetailSerializer,
    }
    queryset = Product.objects.all()
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name']

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = CategorySerializer
    serializer_map = {
        "list": CategoryDetailSerializer,
        "retrieve": CategoryDetailSerializer,
    }
    queryset = Category.objects.all()

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)

class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = StatusSerializer
    serializer_map = {
        "list": StatusDetailSerializer,
        "retrieve": StatusDetailSerializer,
    }
    queryset = Status.objects.all()

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)

class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = BrandSerializer
    serializer_map = {
        "list": BrandDetailSerializer,
        "retrieve": BrandDetailSerializer,
    }
    queryset = Brand.objects.all()

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)

class SeriesViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = SeriesSerializer
    serializer_map = {
        "list": SeriesDetailSerializer,
        "retrieve": SeriesDetailSerializer,
    }
    queryset = Series.objects.all()

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)

class CharacterViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = CharacterSerializer
    serializer_map = {
        "list": CharacterDetailSerializer,
        "retrieve": CharacterDetailSerializer,
    }
    queryset = Character.objects.all()

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = TagSerializer
    serializer_map = {
        "list": TagDetailSerializer,
        "retrieve": TagDetailSerializer,
    }
    queryset = Tag.objects.all()

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)

class SportViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = SportSerializer
    serializer_map = {
        "list": SportDetailSerializer,
        "retrieve": SportDetailSerializer,
    }
    queryset = Sport.objects.all()

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)
    