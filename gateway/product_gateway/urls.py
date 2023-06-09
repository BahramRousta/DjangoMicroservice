from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListGateWay

app_name = 'products'

router = DefaultRouter()

router.register('list', ProductListGateWay, basename='list/')


urlpatterns = [
    path('', include(router.urls)),
]