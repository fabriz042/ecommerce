from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view
from .schema_docs import products_list_docs

from .models import (Product)
from .serializer import (ProductSerializer, ProductDetailSerializer)
from .permissions import (ProductPermission)
from utils.CustomPagination import CustomPagination

@extend_schema_view(
    list=products_list_docs
)

class ProductsView(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = ProductSerializer
    serializer_map = {
        "list": ProductDetailSerializer,
        "retrieve": ProductDetailSerializer,
    }
    queryset = Product.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)