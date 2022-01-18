from django.http import HttpResponse
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


def index(request):
    return HttpResponse(
        "Hello, world. You're at the catalog index. "
        f"There are {Product.objects.count()} products."
    )


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



