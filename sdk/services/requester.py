from sdk.httpp.base import HttpClient
from sdk.config import DEFAULT_BASE_URL


class RequesterService:
    def __init__(self, app_id: str, client: HttpClient, base_url: str):
        self.client = client
        self.app_id = app_id
        self.base_url = base_url or DEFAULT_BASE_URL

    def get(self, path, params):
        full_url_path = self.base_url.rstrip('/') + path
        params = {**params, 'app_id': self.app_id}

        return self.client.get(full_url_path, params=params)

