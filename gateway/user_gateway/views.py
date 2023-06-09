from core.views import GateWayView


class AuthLoginGateWay(GateWayView):

    def create(self, request):
        url = 'http://127.0.0.1:8002/login/'
        return self._send_request(request, url)


class AuthRegisterGateWay(GateWayView):

    def create(self, request):
        url = 'http://127.0.0.1:8002/register/'
        return self._send_request(request, url)


class AuthLogOutGateWay(GateWayView):

    def create(self, request):
        url = 'http://127.0.0.1:8002/logout/'
        return self._send_request(request, url)
