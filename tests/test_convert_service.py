import pytest
from sdk.transport.response import Response


def test_convert_service_path(converter_service, monkeypatch):
    data = {}

    def fake_get(url, params=None):
        data['url'] = url
        data['params'] = params
        return Response(200, {'ok': True})

    monkeypatch.setattr(converter_service._request_service.client, 'get', fake_get)

    res = converter_service.convert(100, 'USD', 'EUR')
    assert res.status_code == 200
    assert data['url'].endswith("/convert/100/USD/EUR")


@pytest.mark.parametrize('amount', [1, 1.0, 123.45])
def test_convert_service_amount_types(converter_service, monkeypatch, amount):
    data = {}

    def fake_get(url, params=None):
        data['url'] = url
        data['params'] = params
        return Response(200, {})

    monkeypatch.setattr(converter_service._request_service.client, 'get', fake_get)

    converter_service.convert(amount, 'USD', 'AED')
    assert str(amount) in data['url']


def test_convert_prettyprint_default_false(converter_service, monkeypatch):
    data = {}

    def fake_get(url, params=None):
        data["params"] = params
        return Response(200, {})

    monkeypatch.setattr(converter_service._request_service.client, 'get', fake_get)

    converter_service.convert(100, "USD", "EUR")
    assert data["params"]["prettyprint"] is False


def test_convert_response_passthrough(converter_service, monkeypatch):
    expected = Response(200, {"rate": 0.9})

    def fake_get(url, params=None):
        return expected

    monkeypatch.setattr(converter_service._request_service.client, 'get', fake_get)

    resp = converter_service.convert(100, "USD", "EUR")
    assert resp is expected
