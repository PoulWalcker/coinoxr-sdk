import requests

from sdk.httpp.base import HttpClient
from sdk.httpp.response import Response


class StubClient(HttpClient):
    def get(self, url, params=None) -> Response:
        return Response(200, {'data': 'fake get request'})
