# -*- coding: utf-8 -*-
"""
Robust Yahoo Finance scraper using yahooquery (no scraping, real API)

This fetches AAPL's annual and quarterly income statements.
"""

from yahooquery import Ticker
import pandas as pd

def fetch_income(ticker_symbol="AAPL"):
    """
    Retrieves both annual and quarterly income statements using yahooquery.
    Returns: (annual_df, quarterly_df)
    """
    t = Ticker(ticker_symbol)
    annual_df = t.income_statement(frequency='annual')
    quarterly_df = t.income_statement(frequency='quarterly')
    return annual_df, quarterly_df

def main():
    ticker = "AAPL"
    print(f"\n📊 Fetching income statements for {ticker} via yahooquery...")

    try:
        annual_df, quarterly_df = fetch_income(ticker)
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return

    if isinstance(annual_df, pd.DataFrame) and not annual_df.empty:
        print("\n✅ Annual Income Statement:")
        print(annual_df.head(1).T)
        annual_df.to_csv(f"{ticker}_income_annual.csv")
        print(f"💾 Saved as {ticker}_income_annual.csv")
    else:
        print("⚠️ No annual income data available.")

    if isinstance(quarterly_df, pd.DataFrame) and not quarterly_df.empty:
        print("\n✅ Quarterly Income Statement:")
        print(quarterly_df.head(1).T)
        quarterly_df.to_csv(f"{ticker}_income_quarterly.csv")
        print(f"💾 Saved as {ticker}_income_quarterly.csv")
    else:
        print("⚠️ No quarterly income data available.")

if __name__ == "__main__":
    main()

# # ============================================================================
# # Getting financial data from yahoo finance using webscraping - Intro
# # Author - Mayank Rasu

# # Please report bugs/issues in the Q&A section
# # =============================================================================

# import requests
# from bs4 import BeautifulSoup

# income_statement = {}

# url = "https://finance.yahoo.com/quote/AAPL/financials?p=AAPL"

# headers = {"User-Agent" : "Chrome/96.0.4664.110"}
# page = requests.get(url, headers=headers)
# page_content = page.content
# soup = BeautifulSoup(page_content,"html.parser")
# tabl = soup.find_all("div" , {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
# for t in tabl:
#     rows = t.find_all("div" , {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
#     for row in rows:
#         income_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1]
