from sdk.services.requester import RequesterService


class CurrenciesService:
    def __init__(self, requester_service: RequesterService):
        self._request_service = requester_service

    def get(self, pretty_print=False, show_alternative=False, show_inactive=False):
        params = {
            'pretty_print': pretty_print,
            'show_alternative': show_alternative,
            'show_inactive': show_inactive
        }

        return self._request_service.get('/currencies.json', params)


