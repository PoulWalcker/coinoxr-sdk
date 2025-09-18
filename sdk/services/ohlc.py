from sdk.services.requester import RequesterService
from sdk.utils.dates import ensure_date
from sdk.transport.types import Params
from sdk.exceptions import ValidationError


class OhlcService:
    """Service for /ohlc.json endpoint"""

    def __init__(self, requester_service: RequesterService):
        self._request_service = requester_service

    def ohlc(
        self,
        start: str,
        period: str,
        base: str | None = None,
        symbols: str | None = None,
        pretty_print: bool = False,
        show_alternative: bool = False,
    ):
        if not ensure_date(start, "%Y-%m-%dT%H:%M:%SZ"):
            raise ValidationError(
                "Invalid datetime format, expected YYYY-MM-DDThh:mm:ssZ"
            )

        params: Params = {
            'start': start,
            'period': period,
            'prettyprint': pretty_print,
            'show_alternative': show_alternative,
        }

        if base is not None:
            params['base'] = base

        if symbols is not None:
            params['symbols'] = symbols

        return self._request_service.get('/ohlc.json', params)
