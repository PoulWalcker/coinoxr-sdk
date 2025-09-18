import requests

from sdk.transport.base import HttpClient
from sdk.transport.response import Response
from sdk.exceptions import NetworkError


class RequestsClient(HttpClient):
    """HTTP client based on the requests library"""

    def get(self, url: str, params: dict | None = None) -> Response:
        """Send GET request and return SDK Response"""
        try:
            response = requests.get(url, params=params)
            return self._wrap_response(response)

        except requests.RequestException as e:
            raise NetworkError(str(e)) from e

    def _wrap_response(self, r: requests.Response) -> Response:
        """Wrap requests.Response into SDK Response"""
        try:
            body = r.json()
        except ValueError:
            body = None
        return Response(r.status_code, body)
