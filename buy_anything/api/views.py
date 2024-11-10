from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ProductSerializer, SubCategorySerializer, CategorySerializer, ProductItemSerializer, \
	VariationTypeSerializer, VariationClassSerializer, \
	ProductListSerializer, ProductItemListSerializer
from .models import Product, SubCategory, Category, ProductItem, VariationType, VariationClass


##################################################################
## LIST API VIEWS
##################################################################
class ProductListAPIView(ListAPIView):
	serializer_class = ProductListSerializer
	queryset = Product.objects.all()
	permission_classes = [AllowAny]
	
class SubCategoryListAPIView(ListAPIView):
	serializer_class = SubCategorySerializer
	queryset = SubCategory.objects.all()
	permission_classes = [AllowAny]
	
class CategoryListAPIView(ListAPIView):
	serializer_class = CategorySerializer
	queryset = Category.objects.all()
	permission_classes = [AllowAny]
	
class ProductItemListAPIView(ListAPIView):
	serializer_class = ProductItemListSerializer
	queryset = ProductItem.objects.all()
	permission_classes = [AllowAny]
	
	def post(self, request):
		data = request.data
		serializer = self.serializer_class(data)
		serializer.save()
		return Response(status=status.HTTP_201_CREATED)
		
	
	# def post(self):
	
# class VariationTypeListAPIView(ListAPIView):
# 	serializer_class = VariationTypeSerializer
# 	queryset = VariationType.objects.all()
# 	permission_classes = [AllowAny]
#
# class VariationClassListAPIView(ListAPIView):
# 	serializer_class = VariationClassSerializer
# 	queryset = VariationClass.objects.all()
# 	permission_classes = [AllowAny]
	
##################################################################

##################################################################
# DETAIL API VIEWS
##################################################################

######################
# BASE DETAIL API VIEWS
#####################
class BaseDetailView(APIView):
	serializer_class = None
	permission_classes = [AllowAny]
	model = None
	
	def get(self, request, id):
		obj = get_object_or_404(self.model, pk=id)
		serializer = self.serializer_class(obj)
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	def patch(self, request, id):
		obj = get_object_or_404(self.model, pk=id)
		serializer = self.serializer_class(obj, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(BaseDetailView):
	serializer_class = ProductSerializer
	permission_classes = [AllowAny]
	model = Product

class CategoryDetailView(BaseDetailView):
	serializer_class = CategorySerializer
	permission_classes = [AllowAny]
	model = Category
	
class SubCategoryDetailView(BaseDetailView):
	serializer_class = SubCategorySerializer
	permission_classes = [AllowAny]
	model = SubCategory
	
class ProductItemDetailView(BaseDetailView):
	serializer_class = ProductItemSerializer
	permission_classes = [AllowAny]
	model = ProductItem


class ProductVariationView(BaseDetailView):
	serializer_class = ProductItemSerializer
	
	def get(self, request, id):
		product = get_object_or_404(Product, pk=id)
		product_items = ProductItem.objects.filter(product=product)
		if not product_items.exists():
			return Response({'error': 'No Product variations exist for given product id'}, status=status.HTTP_404_NOT_FOUND)
		serializer = self.serializer_class(product_items, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

##################################################################

