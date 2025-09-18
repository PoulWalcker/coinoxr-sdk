import pytest
from sdk.exceptions import ValidationError


# helpers
def _params(resp):
    return resp.body["params"]


class TestLatest:
    def test_path(self, rates_services):
        res = rates_services.latest()
        assert res.body["url"].endswith("/latest.json")

    def test_base(self, rates_services):
        res = rates_services.latest(base="USD")
        assert _params(res)["base"] == "USD"

    def test_symbols(self, rates_services):
        res = rates_services.latest(symbols=["USD", "AED"])
        symbols = _params(res)["symbols"]
        assert isinstance(symbols, str)
        assert symbols == "USD,AED"


class TestHistorical:
    def test_path(self, rates_services):
        res = rates_services.historical(date="2025-10-13")
        assert res.body["url"].endswith("/historical/2025-10-13.json")

    def test_base(self, rates_services):
        res = rates_services.historical(date="2025-10-13", base="USD")
        assert _params(res)["base"] == "USD"

    def test_symbols(self, rates_services):
        res = rates_services.historical(date="2025-10-13", symbols=["USD", "EUR"])
        symbols = _params(res)["symbols"]
        assert isinstance(symbols, str)
        assert symbols == "USD,EUR"

    @pytest.mark.parametrize(
        "bad_date",
        [
            "2025/12/01",  # wrong separator
            "2025-13-01",  # invalid month
            "2025-07-35",  # invalid day
            "string",  # not a date at all
        ],
    )
    def test_date_raises(self, rates_services, bad_date):
        with pytest.raises(ValidationError) as excinfo:
            rates_services.historical(date=bad_date)
        assert (
            excinfo.value.args[0]
            == "Invalid date format for 'date', expected YYYY-MM-DD"
        )


class TestTimeSeries:
    def test_path(self, rates_services):
        res = rates_services.time_series(start="2025-01-01", end="2025-02-01")
        assert res.body["url"].endswith("/time-series.json")

    def test_base(self, rates_services):
        res = rates_services.time_series(
            start="2025-01-01", end="2025-02-01", base="USD"
        )
        assert _params(res)["base"] == "USD"

    def test_symbols(self, rates_services):
        res = rates_services.time_series(
            start="2025-01-01", end="2025-02-01", symbols=["USD", "EUR"]
        )
        symbols = _params(res)["symbols"]
        assert isinstance(symbols, str)
        assert symbols == "USD,EUR"

    @pytest.mark.parametrize(
        ("start", "end"),
        [
            ("2025/12/01", "2025-12-30"),  # wrong separator
            ("2025-13-01", "2025-12-30"),  # invalid month
            ("2025-07-35", "2025-07-40"),  # invalid day
            ("string", "2025-12-30"),  # not a date at all
            ("2025-01-01", "string"),  # bad end date
        ],
    )
    def test_date_raises(self, rates_services, start, end):
        with pytest.raises(ValidationError) as excinfo:
            rates_services.time_series(start=start, end=end)
        assert excinfo.value.args[0].startswith("Invalid date format")

    def test_start_after_end_raises(self, rates_services):
        with pytest.raises(ValidationError) as excinfo:
            rates_services.time_series(start="2025-01-02", end="2025-01-01")
        assert excinfo.value.args[0].startswith("'start' must be <= 'end'")
