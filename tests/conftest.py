import pytest
from sdk.transport.base import HttpClient
from sdk.services.requester import RequesterService
from sdk.transport.stub_client import StubClient
from sdk.services.currencies import CurrenciesService
from sdk.services.rates import RatesService
from sdk.services.converter import ConverterService
from sdk.services.ohlc import OhlcService


@pytest.fixture
def stub_client() -> HttpClient:
    return StubClient()


@pytest.fixture
def requester(stub_client: HttpClient) -> RequesterService:
    return RequesterService(app_id='test_key', client=stub_client)


@pytest.fixture
def currencies_services(requester):
    return CurrenciesService(requester)


@pytest.fixture
def rates_services(requester):
    return RatesService(requester)


@pytest.fixture
def converter_service(requester):
    return ConverterService(requester)


@pytest.fixture
def ohlc_service(requester):
    return OhlcService(requester)
