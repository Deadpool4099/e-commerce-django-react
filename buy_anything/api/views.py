from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import ProductSerializer
from .models import Product


class ProductListAPIView(ListAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()
	permission_classes = [AllowAny]



