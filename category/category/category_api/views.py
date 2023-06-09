from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from .models import Category
from rest_framework import viewsets, status
from .serializers import CategorySerializer


class CategoryView(viewsets.ViewSet):

    serializer_class = CategorySerializer

    def list(self, request):
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
            serializer = self.serializer_class(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(
                data={
                    'message': 'Category dose not exist.'
                },
                status=status.HTTP_404_NOT_FOUND
            )