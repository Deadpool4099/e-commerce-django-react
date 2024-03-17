from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SignupView, ActivateView, SigninView, SignoutView, HomeView

# Define DRF router
router = DefaultRouter()

# Register your views with the router
# router.register(r'signup', SignupView, basename='signup')
# router.register(r'signout', SignoutView, basename='signout')

# Define your custom paths
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('activate/<uidb64>/<token>', ActivateView.as_view(), name='activate'),
    path('signin', SigninView.as_view(), name='signin'),
    path('signout', SignoutView.as_view(), name='signout'),
    path('signup', SignupView.as_view(), name='signup'),
]

# Include the DRF router URLs
urlpatterns += router.urls
