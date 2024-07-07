import yfinance as yf
import pandas as pd
import mplfinance as mpf

# i want to analyse the tickers from "ticker"
tickers = ['PETR4.SA', 'AAPL', 'GOOGL']

# here i define what ticker i want to analyse and the interval
for ticker in tickers:
    data = yf.download(ticker, start='2024-01-01', end='2024-07-07')
    data.index.name = 'Date'
    mpf.plot(data, type='candle', style='charles', title='Candlestick Chart (2024-01 > 2024-07)',
         ylabel='Price USD', volume=True, show_nontrading=True, savefig=f"{ticker}_candlestick_chart.png")
