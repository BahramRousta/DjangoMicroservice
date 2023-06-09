from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ShopSerializer


class ShopView(viewsets.ViewSet):

    serializer_class = ShopSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


