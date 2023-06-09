from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'shop'

router = DefaultRouter()
router.register(r'shops', ShopView, basename='shop')

urlpatterns = [

    path('shops/create/',
         ShopView.as_view({'post': 'create'}),
         name='shop-create'),
]