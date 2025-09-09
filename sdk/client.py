from sdk.services.currencies import CurrenciesService
from sdk.services.requester import RequesterService

from sdk.httpp.request_client import RequestsClient


class CoinoxrClient:
    def __init__(self, app_id: str, http_client=None, base_url: str | None = None):
        self.client = http_client or RequestsClient()
        self._requester_service = RequesterService(app_id, self.client, base_url)

        self.currencies = CurrenciesService(self._requester_service)
