from django.urls import path
from .views import ProductListAPIView, CategoryListAPIView, SubCategoryListAPIView, \
    ProductDetailView, CategoryDetailView, SubCategoryDetailView, ProductItemListAPIView, \
    ProductItemDetailView, ProductVariationView

# API URL patterns
urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='list-products'),
    path('categories/', CategoryListAPIView.as_view(), name='list-categories'),
    path('sub-categories/', SubCategoryListAPIView.as_view(), name='list-sub-categories'),
    path('product-items/', ProductItemListAPIView.as_view(), name='list-product-items'),

    path('products/<uuid:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/<uuid:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('sub-categories/<uuid:id>/', SubCategoryDetailView.as_view(), name='sub-category-detail'),
    path('product-items/<uuid:id>/', ProductItemDetailView.as_view(), name='product-item-detail'),
    
    path('products/<uuid:id>/variations/', ProductVariationView.as_view(), name='product-variations'),

]

