from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('user_gateway.urls')),
    path('api/products/', include('product_gateway.urls')),
]
