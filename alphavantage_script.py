# -*- coding: utf-8 -*-
"""
Extracting financial data using the Alpha Vantage API

This script demonstrates how to:
1. Fetch daily OHLCV Forex data (EUR/USD)
2. Download intraday close prices for multiple tickers
3. Download full OHLCV intraday data for multiple tickers

Includes:
- Detailed technical comments for intermediate learners
- API error handling (e.g., unsupported tickers or rate limits)
- API rate-limit management (5 calls per minute on free tier)
"""

# ==========================
# 📦 Import Required Modules
# ==========================
from alpha_vantage.timeseries import TimeSeries  # Alpha Vantage wrapper for stock/time series data
import pandas as pd                              # For DataFrame structures and tabular manipulation
import time                                      # For timing and API sleep to manage rate limits

# ==========================
# 🔑 Load API Key from File
# ==========================
# Store your personal API key in a text file for security and reusability
key_path = r"D:\Github Projects C\GITHUB PROJECTS DO HERE C\QuantYahoo\QuantYahoo\key.txt"
api_key = open(key_path, 'r').read().strip()  # Ensure we strip out newline or spaces

# ==========================
# 📈 1. Daily Forex OHLCV Data (EUR/USD)
# ==========================
# Initialize TimeSeries object using the API key
ts = TimeSeries(key=api_key, output_format='pandas')

# 'get_daily' returns historical daily OHLCV for currency pair EURUSD
forex_data = ts.get_daily(symbol='EURUSD', outputsize='full')[0]
forex_data.columns = ["open", "high", "low", "close", "volume"]
forex_data = forex_data.iloc[::-1]  # Reversing to chronological order

# Display a sample of the data
print("\n📊 Sample daily Forex OHLCV data (EURUSD):")
print(forex_data.head())

# ==========================
# 📉 2. Intraday Close Prices for Multiple Stocks
# ==========================
# Use updated tickers (e.g. FB → META, GOOG → GOOGL)
safe_tickers = ["AAPL", "MSFT", "CSCO", "AMZN", "GOOGL", "META", "BA", "MMM", "XOM", "NKE", "INTC"]

# DataFrame to store just the closing prices from intraday data
close_prices = pd.DataFrame()
api_call_count = 1
start_time = time.time()
ts = TimeSeries(key=api_key, output_format='pandas')

print("\n📈 Fetching intraday close prices (1-minute interval)...")

# Loop through each ticker and pull intraday 'close' prices
for ticker in safe_tickers:
    try:
        # Fetch compact 1-minute interval data (latest ~100 rows)
        data = ts.get_intraday(symbol=ticker, interval='1min', outputsize='compact')[0]
        data.columns = ["open", "high", "low", "close", "volume"]
        data = data.iloc[::-1]  # Reverse to chronological order
        close_prices[ticker] = data["close"]
        print(f"✅ Added {ticker} to close_prices DataFrame")

        # Handle API call limits: 5 requests per minute for free accounts
        api_call_count += 1
        if api_call_count == 5:
            api_call_count = 1
            time.sleep(60 - ((time.time() - start_time) % 60.0))

    except Exception as e:
        print(f"❌ Failed to fetch intraday close for {ticker}: {e}")

# Display the top rows of the close prices table
print("\n📊 Sample of intraday close prices:")
print(close_prices.head())

# ==========================
# 📦 3. Intraday Full OHLCV for Multiple Stocks
# ==========================
# Dictionary to store full OHLCV per ticker
ohlv_dict = {}
api_call_count = 1
start_time = time.time()
ts = TimeSeries(key=api_key, output_format='pandas')

print("\n📦 Fetching full OHLCV intraday data (1-minute interval)...")

# Loop through each ticker and fetch full OHLCV structure
for ticker in safe_tickers:
    try:
        data = ts.get_intraday(symbol=ticker, interval='1min', outputsize='compact')[0]
        data.columns = ["open", "high", "low", "close", "volume"]
        data = data.iloc[::-1]
        ohlv_dict[ticker] = data
        print(f"✅ Stored full OHLCV data for {ticker}")

        api_call_count += 1
        if api_call_count == 5:
            api_call_count = 1
            time.sleep(60 - ((time.time() - start_time) % 60.0))

    except Exception as e:
        print(f"❌ Failed to fetch OHLCV for {ticker}: {e}")

# Print a sample of OHLCV data for the first stock in list
example_ticker = safe_tickers[0]
print(f"\n🧪 Sample OHLCV data for {example_ticker}:")
print(ohlv_dict[example_ticker].head())
