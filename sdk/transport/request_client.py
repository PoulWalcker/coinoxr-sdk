import requests

from sdk.transport.base import HttpClient
from sdk.transport.response import Response


class RequestsClient(HttpClient):
    """HTTP client based on the requests library"""

    def get(self, url: str, params: dict | None = None) -> Response:
        """Send GET request and return SDK Response"""
        response = requests.get(url, params=params)
        return self._wrap_response(response)

    def _wrap_response(self, response: requests.Response) -> Response:
        """Wrap requests.Response into SDK Response"""
        try:
            return Response(response.status_code, response.json())
        except ValueError:
            return Response(response.status_code, None)
