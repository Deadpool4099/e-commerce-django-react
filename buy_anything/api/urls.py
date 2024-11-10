from django.urls import path




from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductListAPIView


# Define DRF router
router = DefaultRouter()

urlpatterns = [
	path('products/', ProductListAPIView.as_view(), name='list-products'),
]


# Include the DRF router URLs
urlpatterns += router.urls
