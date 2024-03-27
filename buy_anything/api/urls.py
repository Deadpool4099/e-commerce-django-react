from django.urls import path
from .views import ProductItemListAPIView#, ProductListAPIView

urlpatterns = [
    path('products/', ProductItemListAPIView.as_view(), name='product-item-list'),
]
