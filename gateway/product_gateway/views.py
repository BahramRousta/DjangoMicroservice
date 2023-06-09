from core.views import GateWayView


class ProductListGateWay(GateWayView):

    def list(self, request):
        url = 'http://127.0.0.1:8003/products/list/'
        return self._send_request(request, url)