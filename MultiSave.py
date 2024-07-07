'''
The present code get some informations about three big IT companies APPLE, MICROSOFT AND GOOGLE
Using yFinance and the model 'download' we can extract some informations about this companies
(date, open, high, low, close, adjclose and volume) and we can save this information using pandas
in an excel sheet.
'''
import yfinance as yf
import pandas as pd

# Selected tickers to analyse and colect some data
tickers = ['AAPL', 'MSFT', 'GOOGL']

# Creating our excel saver
with pd.ExcelWriter('multiple_tickers_data.xlsx', engine = 'openpyxl') as writer:
    # basically we are saying to the sistem: "for each ticker in a list of many tickers, do this:"
    for ticker in tickers:
        # collection datas in the data interval setted by the user
        data = yf.download(ticker, start="2020-01-01", end="2024-07-07")
        # saving the excel sheets
        data.to_excel(writer, sheet_name=ticker)