from sdk.services.requester import RequesterService
from sdk.transport.types import Params


class ConverterService:
    """Service for currency conversion (/convert endpoint)"""

    def __init__(self, request_service: RequesterService):
        self._request_service = request_service

    def convert(
        self,
        value: float,
        currency_from: str,
        currency_to: str,
        pretty_print: bool = False,
    ):
        path = f'/convert/{value}/{currency_from}/{currency_to}'

        params: Params = {'prettyprint': pretty_print}

        return self._request_service.get(path, params)
