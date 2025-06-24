# ================================================================================
# 📈 Scraping Financial Data from Yahoo Finance using BeautifulSoup

# ================================================================================

# =======================================
# 📦 Import Required Libraries
# =======================================
import requests                         # For making HTTP requests to websites
from bs4 import BeautifulSoup           # For parsing and navigating HTML content

# =======================================
# 🧾 Dictionary to store scraped income statement data
# =======================================
income_statement = {}

# =======================================
# 🌐 Target URL: Yahoo Finance AAPL Financials Page
# =======================================
url = "https://finance.yahoo.com/quote/AAPL/financials?p=AAPL"

# =======================================
# ⚠️ Set custom headers to mimic a real web browser
# =======================================
# This avoids getting blocked by Yahoo's anti-bot protection
headers = {
    "User-Agent": "Chrome/96.0.4664.110"  # Pretend to be Chrome browser
}

# =======================================
# 🌍 Send HTTP GET request to the URL
# =======================================
page = requests.get(url, headers=headers)
page_content = page.content  # Raw HTML content returned from Yahoo Finance

# =======================================
# 🧹 Parse HTML using BeautifulSoup
# =======================================
soup = BeautifulSoup(page_content, "html.parser")  # Turn HTML into searchable object

# =======================================
# 🔍 Locate the main financial data container
# =======================================
# Yahoo wraps the income statement rows in a specific div with unique classes
containers = soup.find_all("div", {
    "class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"
})

# =======================================
# 🔁 Loop through each container and extract rows
# =======================================
for container in containers:
    rows = container.find_all("div", {
        "class": "D(tbr) fi-row Bgc($hoverBgColor):h"
    })
    for row in rows:
        # Extract all text from the row and split by "|"
        # The first element is the financial metric (e.g. "Total Revenue")
        # The second element is the most recent value
        cells = row.get_text(separator="|").split("|")
        if len(cells) >= 2:
            income_statement[cells[0]] = cells[1]

# =======================================
# 🖨️ Print the income statement nicely
# =======================================
print("\n📊 Income Statement Extracted for AAPL:")
for key, value in income_statement.items():
    print(f"{key}: {value}")
