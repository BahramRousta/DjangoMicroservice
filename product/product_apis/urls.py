from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'product_apis'

router = DefaultRouter()
router.register('products', ProductListViewSet, basename='products')
router.register('user_product', UserProductView, basename='user-product')


urlpatterns = [
    path('products/list/',
         ProductListViewSet.as_view({'get': 'list'}),
         name='products-list'),
    
    path('user_product/create/',
         UserProductView.as_view({'post': 'create'}),
         name='product-create'),

    path('user_product/list/',
         UserProductView.as_view({'get': 'list'}),
         name='products-list'),

    path('user_product/<int:pk>/retrieve/',
         UserProductView.as_view({'get': 'retrieve'}),
         name='products-retrieve'),

    path('user_product/<int:pk>/update/',
         UserProductView.as_view({'put': 'update'}),
         name='product-update'),

    path('user_product/<int:pk>/partial_update/',
         UserProductView.as_view({'patch': 'partial_update'}),
         name='product-partial-update'),

    path('user_product/<int:pk>/delete/',
         UserProductView.as_view({'delete': 'destroy'}),
         name='product-delete'),

]