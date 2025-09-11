from sdk.services.requester import RequesterService


class UsageService:
    def __init__(self, requester_service: RequesterService):
        self._request_service = requester_service

    def usage(self, pretty_print=False):

        params = {
            'pretty_print': pretty_print
        }

        return self._request_service.get('/usage.json', params)
