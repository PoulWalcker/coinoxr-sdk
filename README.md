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

1. currencies -> /currencies.json

[WIP]