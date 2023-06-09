import requests
from django.core.cache import cache
from requests import ConnectionError
from rest_framework.permissions import BasePermission


class VerifyJWTToken(BasePermission):
    def has_permission(self, request, view):
        """Verify access token to access View. Send request to User service
        and return True or False if access token be valid."""

        auth_header = request.META.get('HTTP_AUTHORIZATION', None)

        if auth_header is not None:
            auth = auth_header.split()

            if len(auth) != 2 or auth[0].lower() != 'bearer':
                return False

            token = auth[1]
            user_id = cache.get(token)

            if user_id is not None:
                # If the user ID is in the cache, grant permission
                return True

            verify_urls = 'http://127.0.0.1:8001/api/accounts/verify_token/'

            try:
                response = requests.post(verify_urls, json={'token': token})
            except ConnectionError as err:
                return False

            if response.status_code == 200:

                # Cache the user ID for future requests
                user_id = response.json().get('user_id')
                expiration_time = response.json().get('exp') - response.json().get('iat')
                cache.set(token, user_id, timeout=expiration_time)
                return True
        return False
