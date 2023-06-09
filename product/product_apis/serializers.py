import requests
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def validate_category_id(self, attr):
        response = requests.get(f'http://127.0.0.1:8000/api/category/{attr}/')
        if response.status_code != 200:
            raise serializers.ValidationError("Invalid category ID.")
        return attr