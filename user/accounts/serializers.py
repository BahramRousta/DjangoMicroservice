from rest_framework import serializers, status
from user.settings import SIMPLE_JWT
from .models import CustomUser


class RegisterSerialzier(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        username = data['username']
        password = data['password']
        password2 = data['password2']

        if password != password2:
            raise serializers.ValidationError("Passwords do not match.")
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        user = CustomUser.objects.filter(
            username=username
        ).first()

        if user:
            raise serializers.ValidationError('Username already exists.')

        user = CustomUser(
            username=username
        )
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )


class ObtainTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=255)
    access_token_expiration = serializers.CharField(default=f"{SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds} seconds")
    refresh_token = serializers.CharField(max_length=255)
    refresh_token_expiration = serializers.CharField(default=f"{SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds()} seconds")


class VerifyTokenSerializer(serializers.Serializer):
    request = serializers.CharField(required=True)