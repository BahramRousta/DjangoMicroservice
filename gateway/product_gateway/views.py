import requests
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

@api_view(('GET',))
@renderer_classes([JSONRenderer])
def _send_request(request, url):
    try:
        response = requests.get(url=url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
    except requests.exceptions.RequestException as e:
        return Response(
            data={'error': 'Something went wrong, try again a few minutes later ...'},
            status=status.HTTP_400_BAD_REQUEST
        )
    return Response(response.json(), status=response.status_code)


@csrf_exempt
def product_gateways(request, *args, **kwargs):
    print(request.path)
    if request.path == '/api/products/list/':
        print('send')
        return _send_request(request, 'http://127.0.0.1:8003/api/products/list/')
