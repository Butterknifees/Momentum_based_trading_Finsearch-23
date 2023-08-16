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


#execution of trades part we will define functions that would make the trades they would have numbers from 0 to 1.
#the number indicates the weight of how much we would purchase the stock as a percentage of our portfolio size 
def weight_assigning(rsi_values):
    #both rsi values and prev_weights are dictionaries where we have each of the stocks and a particular number from 0 to 1 to tell the 
    #current wieght they had or their rsi value
    ticker_list=[]
    rsi_ticker_list=[]
    for ticker in rsi_values:
        ticker_list+=[ticker]
        rsi_ticker_list+=[rsi_values[ticker]]
    for i in range(len(rsi_ticker_list)):
        for j in range(len(rsi_ticker_list)-1):
                if rsi_ticker_list[j]>=rsi_ticker_list[j+1]:
                    pass
                else:
                    rsi_ticker_list[j],rsi_ticker_list[j+1]=rsi_ticker_list[j+1],rsi_ticker_list[j]
                    ticker_list[j],ticker_list[j+1]=ticker_list[j+1],ticker_list[j]
    #now we have them arranged in terms of largest rsi values what we need to do next is make an algorithm that will assign weights based on the rsi values that we have for the top 5
    #algorithm we can try couple of things we can do
    #keep a minmum weight that each top 5 would have 
    #which would be 12% ie each has a fixed 0.12(just as an example we shall keep this variable but fixed) component added to 
    #this would be the variable part which would be based on how much they are beating each other

    #let us set the rest of the values to 0
    
    total_diff=rsi_ticker_list[0]+rsi_ticker_list[1]+rsi_ticker_list[2]+ rsi_ticker_list[3] -4*rsi_ticker_list[4]
    fixed_percent=0.13
    weights_list=[]
    for i in range(5):
        weights_list+=[ (rsi_ticker_list[i]-rsi_ticker_list[4])*(1-5*fixed_percent)/total_diff + fixed_percent]

    weights={}
    for i in range(len(rsi_ticker_list)):
        if i<5:
            weights[ticker_list[i]]=weights_list[i]
        else:
            weights[ticker_list[i]]=0

    #we are returning a dictionary with the new weights of the stock that we will be holding for the next 15 day period rest that we 
    #had before need to be sold
    return weights
#this function assumes that we already have made the first transcation and our previous porfolio was not empty
def execute_trade(prev_weights,current_portfolioreturn,start_row_number,period):
    #to simplify calculations we shall do 2 things we shall first sell all of our stock that we have in the last cycle 
    #then we shall buy back with the new weights sorry we dont need this to calculate the return in that period
    #so finally just require our old weights and we are done
    percentage_change_weighted=0
    for ticker in prev_weights:
        ticker_file_name= ticker +'.csv'
        ticker_data = pd.read_csv(ticker_file_name)
        percentage_diff=(ticker_data['Close'][start_row_number]-ticker_data['Close'][start_row_number-period])/ticker_data['Close'][start_row_number-period]
        percentage_change_weighted+=percentage_diff*prev_weights[ticker]
    current_portfolioreturn=current_portfolioreturn*(1+percentage_change_weighted)
    return current_portfolioreturn




#lets create the main portfolio part of the code
#in the porfolio for simplicity we shal consider our portfolio size to be so large that we are always able to buy stocks in full
#size ie there is no remaining money that will lie unused because of the stock price being too large
#we will be having n/period number of transaction where n is the total trading days we shall analyse

#initialising the porfolio return to 1
portfolio_return=1
for transaction_date in range(0,250-period,period):
    Rsi_values={}
    for ticker in tickers:
        ticker_file_name= ticker+ '.csv'
        ticker_data=pd.read_csv(ticker_file_name)
    
        Rsi_values[ticker]=Rsi_calc(ticker_data,period,transaction_date)
    weights_dic=weight_assigning(Rsi_values)

    portfolio_return=execute_trade(weights_dic,portfolio_return,transaction_date+period,period)
    print(portfolio_return)
print("hence we have found the porfolio return in the span of 1 year completing 250/15 ie 16 trades")
print((portfolio_return-1)*100,'% is the profit we have earned by using this strategy')
