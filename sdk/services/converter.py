from sdk.services.requester import RequesterService


class ConverterService:
    def __init__(self, request_service: RequesterService):
        self._request_service = request_service

    def convert(self, value: int, currency_from: str, currency_to: str, pretty_print=False):
        path = f'/convert/{value}/{currency_from}/{currency_to}'

        params = {
            'pretty_print': pretty_print
        }

        return self._request_service.get(path, params)