from sdk.services.requester import RequesterService


class RatesService:
    def __init__(self, requester_service: RequesterService):
        self._request_service = requester_service


