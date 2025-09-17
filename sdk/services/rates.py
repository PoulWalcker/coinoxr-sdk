from sdk.services.requester import RequesterService
from sdk.utils.dates import ensure_date
from sdk.transport.types import Params


class RatesService:
    """Service for /latest.json, /historical/{date}.json and /time-series.json endpoints"""

    def __init__(self, requester_service: RequesterService):
        self._request_service = requester_service

    def latest(
        self,
        base: str | None = None,
        symbols: list[str] | None = None,
        pretty_print: bool = False,
        show_alternative: bool = False,
    ):
        params: Params = {'prettyprint': pretty_print, 'show_alternative': show_alternative}

        if base is not None:
            params['base'] = base

        if symbols is not None:
            params['symbols'] = ','.join(symbols)

        return self._request_service.get('/latest.json', params)

    def historical(
        self,
        date: str,
        base: str | None = None,
        symbols: list[str] | None = None,
        pretty_print: bool = False,
        show_alternative: bool = False,
    ):
        if not ensure_date(date, "%Y-%m-%d"):
            raise ValueError("Invalid date format for 'date', expected YYYY-MM-DD")

        path = f'/historical/{date}.json'

        params: Params = {'prettyprint': pretty_print, 'show_alternative': show_alternative}

        if base is not None:
            params['base'] = base

        if symbols is not None:
            params['symbols'] = ','.join(symbols)

        return self._request_service.get(path, params)

    def time_series(
        self,
        start: str,
        end: str,
        base: str | None = None,
        symbols: list[str] | None = None,
        pretty_print: bool = False,
        show_alternative: bool = False,
    ):

        if not ensure_date(start, "%Y-%m-%d"):
            raise ValueError("Invalid date format for 'start', expected YYYY-MM-DD")

        if not ensure_date(end, "%Y-%m-%d"):
            raise ValueError("Invalid date format for 'end', expected YYYY-MM-DD")

        if start > end:
            raise ValueError("'start' must be <= 'end'")

        params: Params = {
            'start': start,
            'end': end,
            'prettyprint': pretty_print,
            'show_alternative': show_alternative,
        }

        if base is not None:
            params['base'] = base

        if symbols is not None:
            params['symbols'] = ','.join(symbols)

        return self._request_service.get('/time-series.json', params)
