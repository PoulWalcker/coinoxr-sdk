import pytest
from sdk.transport.response import Response
from sdk.exceptions import ValidationError


def test_ohlc_path(ohlc_service, monkeypatch):
    data = {}

    def fake_get(url, params=None):
        data["url"] = url
        return Response(200, {})

    monkeypatch.setattr(ohlc_service._request_service.client, "get", fake_get)

    resp = ohlc_service.ohlc("2025-01-01T00:00:00Z", "30m")
    assert resp.status_code == 200
    assert data["url"].endswith("/ohlc.json")


def test_ohlc_base_and_symbols(ohlc_service, monkeypatch):
    data = {}

    def fake_get(url, params=None):
        data["params"] = params
        return Response(200, {})

    monkeypatch.setattr(ohlc_service._request_service.client, "get", fake_get)

    ohlc_service.ohlc(
        "2025-01-01T00:00:00Z",
        "1d",
        base="USD",
        symbols="EUR,AED",
    )

    params = data["params"]
    assert params["base"] == "USD"
    assert params["symbols"] == "EUR,AED"


def test_ohlc_flags(ohlc_service, monkeypatch):
    data = {}

    def fake_get(url, params=None):
        data["params"] = params
        return Response(200, {})

    monkeypatch.setattr(ohlc_service._request_service.client, "get", fake_get)

    ohlc_service.ohlc(
        "2025-01-01T00:00:00Z",
        "1d",
        pretty_print=True,
        show_alternative=True,
    )

    params = data["params"]
    assert params["prettyprint"] is True
    assert params["show_alternative"] is True


@pytest.mark.parametrize(
    "bad_date",
    [
        "2025-01-01",  # missing time part
        "2025-01-01T12:00:00",  # missing Z
        "2025-13-01T00:00:00Z",  # invalid month
        "not-a-date",  # garbage
    ],
)
def test_ohlc_invalid_date_raises(ohlc_service, bad_date):
    with pytest.raises(ValidationError) as excinfo:
        ohlc_service.ohlc(bad_date, "1d")
    assert (
        excinfo.value.args[0]
        == "Invalid datetime format, expected YYYY-MM-DDThh:mm:ssZ"
    )
