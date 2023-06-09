from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('categories', CategoryView, basename='category')

urlpatterns = [
    path('categories_list/', CategoryView.as_view({'get': 'list'}), name='categories-list'),
    path('category/<int:pk>/', CategoryView.as_view({'get': 'retrieve'}), name='category-retrieve'),
]
