from rest_framework import serializers

from shop_api.models import Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'

    def validate_owner_id(self, attrs):
        return attrs

