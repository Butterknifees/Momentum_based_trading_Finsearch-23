import pandas as pd
import numpy as np

from pandas_datareader import data
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import datetime
import yfinance as yf


from pandas_datareader import data as web

tickers = [ 'AAPL','MSFT', 'GOOGL', 'AMZN', 'TSLA', 'JPM', 'V', 'JNJ', 'NVDA',
           'MA', 'PG', 'INTC', 'HD', 'UNH', 'DIS', 'VZ', 'ADBE', 'CRM', 'PYPL',
           'CMCSA', 'PFE', 'ABT', 'KO', 'T', 'BAC', 'NFLX', 'WMT', 'ASML', 'XOM',
           'CSCO', 'ORCL', 'TMO', 'NKE', 'CVX', 'PEP', 'MRK', 'ABBV', 'AMGN', 'TSM',
           'COST', 'ACN', 'MCD', 'BA', 'AMD', 'WFC', 'IBM', 'NEE', 'PM', 'WBA']

def Rsi_calc(ticker_data,period, start_row):
    #this function will take the start_row, period, and the ticker's one year data
    #the output will be the RSI_value for that 
    gain=0
    loss=0
    for row_number in range(start_row+1,period+1+start_row):
        diff=ticker_data["Close"][row_number]-ticker_data["Close"][row_number-1]
        diff_percent=diff/ticker_data["Close"][row_number]
        if diff_percent<0:
            loss-=diff_percent
        else:
            gain+=diff_percent
    RSI_value= 100- 100/(1+(gain/loss))
    return RSI_value
        
period=14

def 
