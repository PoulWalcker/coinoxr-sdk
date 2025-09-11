# coinoxr-python

Unofficial Python SDK for the [Open Exchange Rates](https://openexchangerates.org/) API.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
from sdk.client import CoinoxrClient

client = CoinoxrClient(app_id="your_api_key")

# List available currencies
currencies = client.currencies.get()
print(currencies)
```

## Services

### currencies
- **Endpoint:** `/currencies.json`  
- **Method:** `client.currencies.get()`

### rates
- **Endpoints:**
  - `/latest.json` → `client.rates.latest(base="USD", symbols=["EUR","GBP"])`
  - `/historical/{YYYY-MM-DD}.json` → `client.rates.historical(date="2025-01-01", base="USD", symbols=["EUR"])`
  - `/time-series.json` → `client.rates.time_series(start="2025-01-01", end="2025-01-31", base="USD", symbols=["EUR","GBP"])`

### convert
- **Endpoint:** `/convert`  
- **Method:** `client.convert.convert("USD", "EUR", 100)`  

### ohlc
- **Endpoint:** `/ohlc.json`  
- **Method:** `client.ohlc.ohlc(start="2025-01-01T00:00:00Z", period="daily", base="USD", symbols=["EUR","GBP"])`  

### usage
- **Endpoint:** `/usage.json`  
- **Method:** `client.usage.usage()`  


[WIP]