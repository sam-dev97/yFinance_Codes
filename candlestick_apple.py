import yfinance as yf
import pandas as pd
import mplfinance as mpf

# i want to analyse the tickers from "ticker"
ticker = 'PETR4.SA'

# here i define what ticker i want to analyse and the interval
data = yf.download(ticker, start='2024-01-01', end='2024-07-07')

# converting data type
data.index.name = 'Date'

# ploting the candlestick grapich
mpf.plot(data, type='candle', style='charles', title=' {ticker} Candlestick Chart (2024-01 > 2024-07)',
         ylabel='Price USD', volume=True, show_nontrading=True)