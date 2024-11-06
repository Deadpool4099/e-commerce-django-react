from rest_framework import serializers
from .models import ProductItem, VariationCombination, ProductCategory


class VariationCombinationSerializer(serializers.ModelSerializer):
    variation_type = serializers.CharField(source='variation_class.variation_type.name')
    variation_class = serializers.CharField(source='variation_class.value')

    class Meta:
        model = VariationCombination
        fields = ['variation_type', 'variation_class']


class ProductItemSerializer(serializers.ModelSerializer):
    variation_combination = VariationCombinationSerializer(many=True, read_only=True)

    class Meta:
        model = ProductItem
        fields = ['id', 'product', 'price', 'stock_available', 'discount', 'variation_combination']


class ProductItemWithDetailsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    # category = serializers.CharField(source='product.product_category.sub_category.category.name')
    # sub_category = serializers.SerializerMethodField()
    """"""
    product_id = serializers.UUIDField(source='product.id')
    product_description = serializers.CharField(source='product.description')
    product_item_price = serializers.IntegerField(source='price')
    product_item_quantity = serializers.IntegerField(source='stock_available')
    product_item_discount = serializers.IntegerField(source='discount')
    # product_sub_category = serializers.CharField(source='product.sub_category.name')
    # product_category = serializers.CharField(source='product.sub_category.category.name')

    # variation_combination = VariationCombinationSerializer(many=True, source='variationcombination_set')

    # def get_sub_category(self, obj):
    #     return [obj.product.product_category.sub_category.name]

    class Meta:
        model = ProductItem
        fields = ['id', 'product_id', 'product_name',
                  'product_description', 'product_item_price', 'product_item_quantity', 'product_item_discount',
                  'product_sub_category', 'product_category',
                  'variation_combination']
        