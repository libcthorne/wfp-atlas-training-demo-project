from django.http import HttpResponse
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


def index(request):
    product_count = Product.objects.count()
    return HttpResponse(
        f"Hello, world. There are {product_count} products."
    )

# Product()
# Product()
# Product()
# response = client.get("/products/") (send request)
# assert response.status_code == 200
# assert response.body == "Hello, world. There are 3 products."


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.filter(
            sellable=True,
        )
        return qs
