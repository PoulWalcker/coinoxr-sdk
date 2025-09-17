from sdk.transport.base import HttpClient
from sdk.transport.types import Params
from sdk.config import DEFAULT_BASE_URL


class RequesterService:
    """Service that builds full API requests and attaches app_id"""

    def __init__(self, app_id: str, client: HttpClient, base_url: str | None = None):
        self.client = client
        self.app_id = app_id
        self.base_url = base_url or DEFAULT_BASE_URL

    def get(self, path: str, params: Params | None = None):
        full_url_path = self.base_url.rstrip('/') + path
        params = {**(params or {}), 'app_id': self.app_id}

        return self.client.get(full_url_path, params=params)
