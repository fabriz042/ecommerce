from rest_framework import viewsets

from .models import (Product)
from .serializer import (ProductSerializer, ProductDetailSerializer)
from .permissions import (ReadOnlyOrIsAuthenticated)
from utils.CustomPagination import CustomPagination

class ProductsView(viewsets.ModelViewSet):
    permission_classes = [ReadOnlyOrIsAuthenticated]
    serializer_class = ProductSerializer
    serializer_map = {
        "list": ProductDetailSerializer,
        "retrieve": ProductDetailSerializer,
    }
    queryset = Product.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)