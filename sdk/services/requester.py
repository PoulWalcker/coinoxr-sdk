from sdk.transport.base import HttpClient
from sdk.transport.types import Params
from sdk.config import DEFAULT_BASE_URL
from sdk.exceptions import APIError, ERROR_MAP


class RequesterService:
    """Service that builds full API requests and attaches app_id"""

    def __init__(self, app_id: str, client: HttpClient, base_url: str | None = None):
        self.client = client
        self.app_id = app_id
        self.base_url = base_url or DEFAULT_BASE_URL

    def get(self, path: str, params: Params | None = None):
        full_url_path = self.base_url.rstrip('/') + path
        params = {**(params or {}), 'app_id': self.app_id}
        res = self.client.get(full_url_path, params=params)

        if 200 <= res.status_code < 300:
            return res

        body = res.body if isinstance(res.body, dict) else {}
        code = body.get('message', '')  # e.g: not_found
        message = body.get('description') or body.get('error') or 'API Error'

        err_cls = ERROR_MAP.get((res.status_code, code), APIError)
        raise err_cls(
            status=res.status_code,
            code=code,
            message=message,
            endpoint=path,
            payload=body,
        )
