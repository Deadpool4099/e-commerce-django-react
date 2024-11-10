from decimal import Decimal

from rest_framework import serializers
from .models import Product, Category, SubCategory, ProductItem, VariationType, VariationClass


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
        
class SubCategorySerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()
    
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description', 'category']


class ProductListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'sub_category']
        
class ProductSerializer(serializers.ModelSerializer):
    
    sub_category = SubCategorySerializer()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'sub_category']
        

        

class VariationTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VariationType
        fields = ['id', 'name', 'sub_category']


class VariationClassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VariationClass
        fields = ['id', 'value', 'variation_type']


class ProductItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    variation_type = VariationTypeSerializer()
    variation_class = VariationClassSerializer()
    price_after_discount = serializers.SerializerMethodField(method_name='get_price_after_discount')
    
    class Meta:
        model = ProductItem
        fields = ['id', 'product', 'variation_type', 'variation_class', 'discount',
                  'price', 'stock_available', 'price_after_discount']
    
    def get_price_after_discount(self, product_item: ProductItem):
        return Decimal(product_item.price) - Decimal(0.01) * product_item.discount * Decimal(product_item.price)


class ProductItemListSerializer(serializers.ModelSerializer):
    price_after_discount = serializers.SerializerMethodField(method_name='get_price_after_discount', read_only=True)
    
    class Meta:
        model = ProductItem
        fields = ['id', 'product', 'variation_type', 'variation_class', 'discount',
                  'price', 'stock_available', 'price_after_discount']
    
    def get_price_after_discount(self, product_item: ProductItem):
        return Decimal(product_item.price) - Decimal(0.01) * product_item.discount * Decimal(product_item.price)


# class ProductVariationSerializer(serializers.ModelSerializer):
#
#     id =

