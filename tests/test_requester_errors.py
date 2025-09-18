import pytest
from sdk.transport.response import Response
from sdk.exceptions import ERROR_MAP, APIError


@pytest.mark.parametrize(
    "status, code, expected_exc",
    [
        (401, "missing_app_id", ERROR_MAP[(401, "missing_app_id")]),
        (401, "invalid_app_id", ERROR_MAP[(401, "invalid_app_id")]),
        (403, "access_restricted", ERROR_MAP[(403, "access_restricted")]),
        (403, "not_allowed", ERROR_MAP[(403, "not_allowed")]),
        (429, "not_allowed", ERROR_MAP[(429, "not_allowed")]),
        (404, "not_found", ERROR_MAP[(404, "not_found")]),
        (400, "invalid_base", ERROR_MAP[(400, "invalid_base")]),
    ],
)
def test_error_map(monkeypatch, requester, status, code, expected_exc):
    def fake_get(url, params=None):
        return Response(status, {"message": code, "description": "test error"})

    monkeypatch.setattr(requester.client, "get", fake_get)

    with pytest.raises(expected_exc) as excinfo:
        requester.get("/")
    err = excinfo.value
    assert isinstance(err, expected_exc)
    assert err.status == status
    assert err.code == code
    assert "test error" in err.message


def test_fallback_to_api_error(monkeypatch, requester):
    body = {"message": "weird_new_code", "description": "???"}

    def fake_get(url, params=None):
        return Response(400, body)

    monkeypatch.setattr(requester.client, "get", fake_get)

    with pytest.raises(APIError) as excinfo:
        requester.get("/latest.json")

    err = excinfo.value
    assert type(err) is APIError
    assert err.status == 400
    assert err.code == "weird_new_code"
    assert err.message == "???"
    assert err.endpoint == "/latest.json"
    assert err.payload == body
