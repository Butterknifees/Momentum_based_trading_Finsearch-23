#this file will use the yahoo finance library to get all the data we require and store it in multiple csv files so that we don't have to redownload the file 
#multiple times 
import yfinance as yf
import csv
import datetime
import pandas as pd
tickers = [ 'AAPL','MSFT', 'GOOGL', 'AMZN', 'TSLA', 'JPM', 'V', 'JNJ', 'NVDA',
           'MA', 'PG', 'INTC', 'HD', 'UNH', 'DIS', 'VZ', 'ADBE', 'CRM', 'PYPL',
           'CMCSA', 'PFE', 'ABT', 'KO', 'T', 'BAC', 'NFLX', 'WMT', 'ASML', 'XOM',
           'CSCO', 'ORCL', 'TMO', 'NKE', 'CVX', 'PEP', 'MRK', 'ABBV', 'AMGN', 'TSM',
           'COST', 'ACN', 'MCD', 'BA', 'AMD', 'WFC', 'IBM', 'NEE', 'PM', 'WBA']
           
start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime(2022, 12, 31)

for ticker in tickers:
    
    data = yf.download(ticker, start=start_date, end=end_date)  # Retrieve data for the current ticker
    data["Ticker"]= ticker  # Append the current ticker symbol to the ticker column
    data.to_csv(ticker+'.csv')
