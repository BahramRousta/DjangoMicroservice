import requests
from rest_framework import viewsets
from rest_framework.response import Response


class GateWayView(viewsets.ViewSet):
    safe_method_map = {
        'GET': requests.get,
        'HEAD': requests.head,
        'OPTIONS': requests.options
    }

    unsafe_method_map = {
        'POST': requests.post,
        'PUT': requests.put,
        'PATCH': requests.patch,
        'DELETE': requests.delete,
    }

    def _send_request(self, request, url):
        try:
            if request.method in self.safe_method_map:
                response = self.safe_method_map[request.method](url)
            elif request.method in self.unsafe_method_map:
                response = self.unsafe_method_map[request.method](url, request.data)
        except requests.exceptions.HTTPError as he:
            return Response(
                he,
                status=400
            )
        except requests.exceptions.RequestException as re:
            return Response(
                data={'error': 'Something went wrong, try again a few minute later ...'},
                status=400
            )

        return Response(response.json(), status=response.status_code)