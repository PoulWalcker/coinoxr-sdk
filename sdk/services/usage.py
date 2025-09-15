from sdk.services.requester import RequesterService


class UsageService:
    """Service for /usage.json endpoint"""

    def __init__(self, requester_service: RequesterService):
        self._request_service = requester_service

    def get(self, pretty_print: bool = False):

        params = {'prettyprint': pretty_print}

        return self._request_service.get('/usage.json', params)
