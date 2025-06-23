# -*- coding: utf-8 -*-
"""
Getting stock data using yfinance (Yahoo Finance API wrapper)

This script demonstrates how to:
1. Download intraday stock data by period and interval
2. Download historical data by specifying a start and end date
3. Print and inspect the resulting DataFrame

"""

import yfinance as yf  # Yahoo Finance API for stock data retrieval

# ========================================
# ⏱️ 1. Get recent intraday OHLCV data (5-minute intervals for 1 month)
# ========================================
# This is useful for high-frequency trading or short-term trend analysis
data_intraday = yf.download("MSFT", period='1mo', interval="5m")

print("\n📊 Intraday 5-minute data (last 1 month):")
print(data_intraday.head())  # Show first 5 rows for inspection
print(f"Total rows: {len(data_intraday)}")
print(f"Available columns: {data_intraday.columns.tolist()}\n")


# ========================================
# 📅 2. Get historical daily OHLCV data from fixed date range
# ========================================
# This is useful for long-term backtesting, investing strategies, or forecasting
data_historical = yf.download("MSFT", start="2017-01-01", end="2020-04-24")

print("📆 Historical daily data from 2017 to April 2020:")
print(data_historical.head())  # Show first 5 rows
print(f"Total rows: {len(data_historical)}")
print(f"Date range: {data_historical.index.min().date()} to {data_historical.index.max().date()}\n")


# ========================================
# 🔁 3. Download intraday data again (technically redundant, included for demonstration)
# ========================================
# Same as the first call — included here to show that calls can be repeated
data_intraday_repeat = yf.download("MSFT", period='1mo', interval="5m")

print("♻️ Re-downloaded intraday data (should match first):")
print(data_intraday_repeat.tail())  # Show last 5 rows
print(f"Total rows: {len(data_intraday_repeat)} (should match earlier intraday download)\n")

# ========================================
# 💾 Optional: Save to CSV for exploration or backup
# ========================================
data_intraday.to_csv("msft_intraday_5min.csv")
data_historical.to_csv("msft_historical_daily.csv")
print("✅ Saved both datasets to CSV files.\n")
