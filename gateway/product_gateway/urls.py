from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import product_gateways

app_name = 'products'
#
# router = DefaultRouter()
#
# router.register('login', product_gateways, basename='login')
#

urlpatterns = [
    path('list/', product_gateways, name='product_gateways'),
]