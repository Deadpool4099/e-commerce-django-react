from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Product, ProductItem

@api_view(['GET'])
@permission_classes([AllowAny])
def product(request):
    pass
    
from rest_framework import generics
from .models import ProductItem
from .serializers import ProductItemWithDetailsSerializer#, ProductCategorySerializer


class ProductItemListAPIView(generics.ListAPIView):
    serializer_class = ProductItemWithDetailsSerializer
    queryset = ProductItem.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        return ProductItem.objects.all()


# class ProductListAPIView(generics.ListAPIView):
#     serializer_class = ProductCategorySerializer
#     queryset = ProductItem.objects.all()
#     permission_classes = [AllowAny]

# from rest_framework import viewsets
# from .models import Product
# from .serializers import ProductSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [AllowAny]


@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_cart_items(request):
    # token_value = request.headers['Authorization']
    # key = token_value.split(' ')[-1]
    # user = Token.objects.get(key=key).user
    pass
