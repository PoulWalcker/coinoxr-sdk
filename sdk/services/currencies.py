from sdk.services.requester import RequesterService
from sdk.transport.types import Params


class CurrenciesService:
    """Service for /currencies.json endpoint"""

    def __init__(self, requester_service: RequesterService):
        self._request_service = requester_service

    def get(
        self,
        pretty_print: bool = False,
        show_alternative: bool = False,
        show_inactive: bool = False,
    ):
        params: Params = {
            'prettyprint': pretty_print,
            'show_alternative': show_alternative,
            'show_inactive': show_inactive,
        }

        return self._request_service.get('/currencies.json', params)
