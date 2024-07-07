import yfinance as yf
import pandas as pd

# Comando básico para baixar dados hisóricos abertura, high, low etc de um ticker dado determinado intervalo
# Nesse exemplo utilizei o código da petrobras, no intervalo de 01/2020 a 07/2024
data = yf.download('PETR4.SA', start='2020-01-01', end='2024-07-07')

# Salvando dados em csv
petroData = data.to_csv('petro.csv')

# Salvando as informações em XLSX(Excel)
data.to_excel('PETR4.xlsx', sheet_name = 'PETR4_DATA')
