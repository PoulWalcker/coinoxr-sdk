from sdk.services.requester import RequesterService
from sdk.transport.types import Params


class UsageService:
    """Service for /usage.json endpoint"""

    def __init__(self, requester_service: RequesterService):
        self._request_service = requester_service

    def get(self, pretty_print: bool = False):

        params: Params = {'prettyprint': pretty_print}

        return self._request_service.get('/usage.json', params)
