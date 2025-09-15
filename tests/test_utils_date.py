import pytest
from datetime import datetime, timezone
from sdk.utils.dates import ensure_date


def test_ensure_date_valid():
    assert ensure_date('2025-09-15', '%Y-%m-%d')


def test_ensure_date_time_valid():
    valid_iso = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert ensure_date(valid_iso, '%Y-%m-%dT%H:%M:%SZ')


@pytest.mark.parametrize('bad_date', [
    "2025/12/01",   # wrong separator
    "2025-13-01",   # invalid month
    "2025-07-35",   # invalid day
    "string",       # not a date at all
])
def test_ensure_date_fail(bad_date):
    assert ensure_date(bad_date, '%Y-%m-%d') is False


@pytest.mark.parametrize("bad_date", [
    "2025/12/01",                  # wrong format
    "2025-12-01T25-12-30Z",        # invalid hour
    "2025-12-01T12-70-30Z",        # invalid minute
    "2025-12-01T12-12-98Z",        # invalid second
])
def test_ensure_datetime_invalid(bad_date):
    assert ensure_date(bad_date, "%Y-%m-%dT%H:%M:%SZ") is False
