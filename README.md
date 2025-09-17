# coinoxr-python

Unofficial Python SDK for the [Open Exchange Rates](https://openexchangerates.org/) API.  
Provides Pythonic services for exchange rates, currency conversion, OHLC and usage endpoints.

> ⚠️ This project is **not affiliated** with Open Exchange Rates.

---

## Installation

From source (development dependencies included):

```bash
pip install -e '.[dev]'
```

When published to PyPI:

```bash
pip install coinoxr-python
```

---

## Quickstart

```python
from sdk import CoinoxrClient

client = CoinoxrClient(app_id="your_api_key")

# List currencies
currencies = client.currencies.get()
print(currencies)

# Latest exchange rates
latest = client.rates.latest(base="USD", symbols=["EUR", "GBP"])
print(latest)

# Convert 100 USD to EUR
converted = client.converter.convert(100, "USD", "EUR")
print(converted)
```

---

## Services

### `currencies`
- **Endpoint:** `/currencies.json`  
- **Method:** `client.currencies.get()`

### `rates`
- `/latest.json` → `client.rates.latest(...)`
- `/historical/{YYYY-MM-DD}.json` → `client.rates.historical(...)`
- `/time-series.json` → `client.rates.time_series(...)`

### `convert`
- **Endpoint:** `/convert`  
- **Method:** `client.converter.convert(100, "USD", "EUR")`

### `ohlc`
- **Endpoint:** `/ohlc.json`  
- **Method:**  
  ```python
  client.ohlc.ohlc(
      start="2025-01-01T00:00:00Z",
      period="daily",
      base="USD",
      symbols=["EUR","GBP"]
  )
  ```

### `usage`
- **Endpoint:** `/usage.json`  
- **Method:** `client.usage.get()`

---

## Development

Run tests:

```bash
pytest -q
```

Lint and format:

```bash
ruff check .
black .
```

---

## License

[MIT](LICENSE)
