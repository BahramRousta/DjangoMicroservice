from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthLoginView, AuthRegisterView, AuthLogOutView

app_name = 'accounts'

router = DefaultRouter()

router.register('login', AuthLoginView, basename='login')
router.register('register', AuthRegisterView, basename='register')
router.register('logout', AuthLogOutView, basename='logout')


urlpatterns = [
    path('', include(router.urls)),
]