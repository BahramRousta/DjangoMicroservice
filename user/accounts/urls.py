from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'accounts'

router = DefaultRouter()


router.register('register', Register, basename='register')
router.register('login', LogIn, basename='login')
router.register('logout', LogOut, basename='logout')
router.register('verify_token', VerifyToken, basename='verify-token')

urlpatterns = [
    path('', include(router.urls)),
]