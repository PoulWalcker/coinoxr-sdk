from sdk.services.requester import RequesterService


class RatesService:
    def __init__(self, requester_service: RequesterService):
        self._request_service = requester_service

    def latest(
            self,
            base: str | None = None,
            symbols: list[str] | None = None,
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
