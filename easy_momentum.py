import pandas as pd
import numpy as np

from pandas_datareader import data
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import datetime
import yfinance as yf


from pandas_datareader import data as web

tickers = [ 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'JPM', 'V', 'JNJ', 'NVDA',
           'MA', 'PG', 'INTC', 'HD', 'UNH', 'DIS', 'VZ', 'ADBE', 'CRM', 'PYPL',
           'CMCSA', 'PFE', 'ABT', 'KO', 'T', 'BAC', 'NFLX', 'WMT', 'ASML', 'XOM',
           'CSCO', 'ORCL', 'TMO', 'NKE', 'CVX', 'PEP', 'MRK', 'ABBV', 'AMGN', 'TSM',
           'COST', 'ACN', 'MCD', 'BA', 'AMD', 'WFC', 'IBM', 'NEE', 'PM', 'WBA']

def Rsi_calc(ticker_data,period):
    #this fucntion will use the ticker data for a period of set days and will find the RSI value for those set days for that stock
    gain=0
    loss=0
    for row_number in range(1,period+1):
        diff=ticker_data["Close"][row_number]-ticker_data["Close"][row_number-1]
        diff_percent=diff/ticker_data["Close"][row_number]
        if diff_percent<0:
            loss-=diff_percent
        else:
            gain+=diff_percent
    RSI_value= 100- 100/(1+(gain/loss))
    return RSI_value
        


start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime(2022, 12, 31)
period=14
days_year=len(yf.download("AAPL",start=start_date,end=end_date))
data= yf.download('AAPL', start=start_date, end=end_date)
data["Ticker"]= "APPL"
print(data)
print(type(data))
for ticker in tickers:
    
    data_of_each_ticker = yf.download(ticker, start=start_date, end=end_date)  # Retrieve data for the current ticker
    data_of_each_ticker["Ticker"]= ticker  # Append the current ticker symbol to the ticker column
    data=data.append(data_of_each_ticker,ignore_index= True)

    
    #data = calculate_adx(data, start_date, end_date, period)
    #print(Rsi_calc(data,period))
    
print(data)
    
