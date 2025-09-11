from abc import ABC, abstractmethod
from sdk.transport.response import Response


class HttpClient(ABC):
    """Abstract HTTP client interface"""

    @abstractmethod
    def get(self, url: str, params: dict | None = None) -> Response:
        """Send GET request"""
        pass
