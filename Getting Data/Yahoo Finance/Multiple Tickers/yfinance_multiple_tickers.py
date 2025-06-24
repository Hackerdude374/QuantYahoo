# -*- coding: utf-8 -*-
"""
Download and organize multi-stock OHLCV and Adjusted Close data using yfinance

This script uses the Yahoo Finance API to:
1. Collect adjusted closing prices for multiple tickers in a single DataFrame.
2. Collect full OHLCV data (Open, High, Low, Close, Volume, Adj Close) in a dictionary.
3. Demonstrate best practices like modular data handling, structured storage, and datetime usage.

Author: (adapted with enhanced technical commentary)
"""

import datetime as dt              # For working with date and time
import yfinance as yf             # Yahoo Finance API wrapper
import pandas as pd               # Powerful library for tabular data (like Excel but programmatic)

# Define a list of tickers across different stock exchanges
stocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS", "3988.HK"]
# - U.S. stocks: Amazon, Microsoft, Intel, Google
# - Indian NSE stock: Infosys (.NS = NSE)
# - Hong Kong stock: Bank of China (.HK = HKEX)

# Define date range: From 360 days ago until today
start = dt.datetime.today() - dt.timedelta(days=360)
end = dt.datetime.today()

# Create an empty DataFrame to store adjusted close prices for all stocks
cl_price = pd.DataFrame()

# Create an empty dictionary to hold full OHLCV data per stock
ohlcv_data = {}

# ================================
# 💾 Loop 1: Download only Adjusted Close prices
# ================================
print("Downloading Adjusted Close prices...")
for ticker in stocks:
    # yf.download returns a DataFrame with columns: Open, High, Low, Close, Adj Close, Volume
    stock_data = yf.download(ticker, start=start, end=end)

    # Extract only the 'Adj Close' column and insert into cl_price with the ticker as the column name
    cl_price[ticker] = stock_data["Close"]
    print(f"Added {ticker} adjusted close to cl_price (rows: {len(stock_data)})")

# Print sample of the combined adjusted close prices
print("\n📈 Sample of combined adjusted close prices:")
print(cl_price.head())

# ================================
# 💾 Loop 2: Download full OHLCV data and store per ticker
# ================================
print("\nDownloading full OHLCV data for each ticker...")
for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker, start=start, end=end)
    print(f"Stored OHLCV data for {ticker} (rows: {len(ohlcv_data[ticker])})")

# Show sample of OHLCV data for one ticker
example_ticker = stocks[0]
print(f"\n🗂️ Sample OHLCV data for {example_ticker}:")
print(ohlcv_data[example_ticker].head())

# ================================
# Optional: Save to CSV for exploration in Excel
# ================================
cl_price.to_csv("adjusted_close_prices.csv")
print("\n✅ Saved adjusted close prices to adjusted_close_prices.csv")

# Save each ticker's OHLCV to its own CSV file
for ticker in stocks:
    ohlcv_data[ticker].to_csv(f"{ticker}_ohlcv.csv")
print("✅ Saved OHLCV data for each ticker to individual CSV files")
