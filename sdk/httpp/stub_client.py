from sdk.httpp.base import HttpClient
from sdk.httpp.response import Response


class StubClient(HttpClient):
    """Stub HTTP client for testing without real network calls"""

    def get(self, url: str, params: dict | None = None) -> Response:
        return Response(
            200,
            {
                "data": "fake get request",
                "url": url,
                "params": params,
            },
        )
