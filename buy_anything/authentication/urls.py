from django.urls import path
from .views import signin, signup, signout, test_token, activate


urlpatterns = [
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('login', signin, name='login'),
    path('logout', signout, name='logout'),
    path('register', signup, name='logout'),
    path('test-token', test_token, name='test_token')
]

