from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthLoginGateWay, AuthRegisterGateWay, AuthLogOutGateWay

app_name = 'accounts'

router = DefaultRouter()

router.register('login', AuthLoginGateWay, basename='login')
router.register('register', AuthRegisterGateWay, basename='register')
router.register('logout', AuthLogOutGateWay, basename='logout')


urlpatterns = [
    path('', include(router.urls)),
]