from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
# from .views import SignupView, ActivateView, SigninView, SignoutView, HomeView
from .views import signin, signup, signout, test_token, activate


# Define DRF router
router = DefaultRouter()

# Register your views with the router
# router.register(r'signup', SignupView, basename='signup')
# router.register(r'signout', SignoutView, basename='signout')

# Define your custom paths
urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
    path('signup', signup, name='signup'),
    path('test_token', test_token, name='test_token')
]

# Include the DRF router URLs
urlpatterns += router.urls
