import requests

from sdk.httpp.base import HttpClient
from sdk.httpp.response import Response


class RequestsClient(HttpClient):
    """HTTP client based on the requests library"""
    def get(self, url: str, params: dict | None = None) -> Response:
        """
        Send GET request.

        Args:
            url: Full request URL.
            params: Query parameters.

        Returns:
            Response: SDK Response object with status code and parsed JSON body.
        """
        response = requests.get(url, params=params)
        return self._wrap_response(response)

    def _wrap_response(self, response: requests.Response) -> Response:
        """Convert requests.Response into SDK Response"""
        try:
            return Response(response.status_code, response.json())
        except ValueError:
            return Response(response.status_code, None)
