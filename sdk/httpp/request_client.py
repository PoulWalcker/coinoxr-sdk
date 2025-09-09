import requests

from sdk.httpp.base import HttpClient
from sdk.httpp.response import Response


class RequestsClient(HttpClient):
    def get(self, url, params=None) -> Response:
        response = requests.get(url, params)
        return self._wrap_response(response)

    def _wrap_response(self, response) -> Response:
        try:
            return Response(response.status_code, response.json())
        except ValueError:
            return Response(response.status_code, None)
