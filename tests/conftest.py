import pytest
from sdk.transport.base import HttpClient
from sdk.services.requester import RequesterService
from sdk.transport.stub_client import StubClient


@pytest.fixture
def stub_client() -> HttpClient:
    return StubClient()


@pytest.fixture
def requester(stub_client: HttpClient) -> RequesterService:
    return RequesterService(app_id='test_key', client=stub_client)
