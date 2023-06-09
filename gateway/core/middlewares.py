import os
from dotenv import load_dotenv
import requests
from django.http import HttpResponse

load_dotenv()


class TokenValidationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if self.requires_token_validation(request):
            token = request.headers.get('Authorization')
            if not token or not self.validate_token(token):
                return self.handle_invalid_token()
        return self.get_response(request)

    def requires_token_validation(self, request):
        return request.path not in ('/api/accounts/login/',
                                    '/api/accounts/register/',
                                    '/api/products/list/')

    def validate_token(self, token):
        try:
            VERIFY_TOKEN_URL = os.environ.get('VERIFY_TOKEN_URL')
            assert VERIFY_TOKEN_URL is not None

            response = requests.post(VERIFY_TOKEN_URL, json={'token': token})
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException:
            return False

    def handle_invalid_token(self):
        return HttpResponse('Invalid token', status=401)
