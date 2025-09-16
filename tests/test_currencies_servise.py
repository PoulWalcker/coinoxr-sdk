def test_currencies_service_end_path(currencies_services):
    res = currencies_services.get()
    assert res.body['url'].endswith('currencies.json')


def test_currencies_service_flags(currencies_services):
    res = currencies_services.get(
        pretty_print=True, show_inactive=True, show_alternative=True
    )
    params = res.body['params']
    assert params["prettyprint"] is True
    assert params["show_alternative"] is True
    assert params["show_inactive"] is True
