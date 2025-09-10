from sdk.services.requester import RequesterService

from datetime import date as d


class RatesService:
    def __init__(self, requester_service: RequesterService):
        self._request_service = requester_service

    def latest(
            self,
            base: str | None = None,
            symbols: str | None = None,
            pretty_print=False,
            show_alternative=False
    ):
        params = {
            'pretty_print': pretty_print,
            'show_alternative': show_alternative
        }

        if base is not None:
            params['base'] = base

        if symbols is not None:
            params['symbols'] = symbols

        return self._request_service.get('/latest.json', params)

    def historical(
            self,
            date: str,
            base: str | None = None,
            symbols: str | None = None,
            pretty_print=False,
            show_alternative=False
    ):
        date_iso = self._convert_date_to_iso(date)
        path = f'/historical/{date_iso}.json'

        params = {
            'pretty_print': pretty_print,
            'show_alternative': show_alternative
        }

        if base is not None:
            params['base'] = base

        if symbols is not None:
            params['symbols'] = symbols

        return self._request_service.get(path, params)

    def time_series(
            self,
            start_date: str,
            end_date: str,
            base: str | None = None,
            symbols: str | None = None,
            pretty_print=False,
            show_alternative=False
    ):
        start_iso = self._convert_date_to_iso(start_date)
        end_iso = self._convert_date_to_iso(end_date)

        params = {
            'start': start_iso,
            'end': end_iso,
            'pretty_print': pretty_print,
            'show_alternative': show_alternative
        }

        if base is not None:
            params['base'] = base

        if symbols is not None:
            params['symbols'] = symbols

        return self._request_service.get('/time-series.json', params)



    @staticmethod
    def _convert_date_to_iso(date: str):
        try:
            return d.fromisoformat(date)
        except ValueError:
            raise ValueError('Invalid date, expected YYYY-MM-DD')
