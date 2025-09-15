from sdk.transport.response import Response


def test_requester_app_id_insert(requester):
    assert requester.app_id == 'test_key'


def test_requester_app_id_added(requester, monkeypatch):
    data = {}

    def fake_get(url: str, params: dict | None = None):
        data['params'] = params
        return Response(200, {})

    monkeypatch.setattr(requester.client, 'get', fake_get)

    requester.get('/latest.json', {'base': 'USD'})

    assert data['params']['app_id'] == 'test_key'
    assert data['params']['base'] == 'USD'


def test_requester_empty_params(requester):
    res = requester.get('/')

    assert res.status_code == 200


def test_requester_full_path(requester, monkeypatch):
    data = {}

    def fake_get(url: str, params: dict | None = None):
        data['url'] = url
        data['params'] = params
        return Response(200, {'ok': True})

    monkeypatch.setattr(requester.client, 'get', fake_get)

    res = requester.get('/latest.json')

    assert res.status_code == 200
    assert data['url'].endswith('/latest.json')


def test_requester_valid_response(requester, monkeypatch):
    data = {}
    fake_response = Response(200, {'ok': True})

    def fake_get(url: str, params: dict | None = None):
        data['url'] = url
        data['params'] = params
        return Response(200, {'ok': True})

    monkeypatch.setattr(requester.client, 'get', fake_get)

    res = requester.get('/latest.json')

    assert res.status_code == fake_response.status_code
    assert res.body == fake_response.body
