import yfinance as yf

import datetime
 
# startDate , as per our convenience we can modify
startDate = datetime.datetime(2019, 5, 31)
 
# endDate , as per our convenience we can modify
endDate = datetime.datetime(2021, 1, 30)
GetFacebookInformation = yf.Ticker("META")
 
# pass the parameters as the taken dates for start and end
print(GetFacebookInformation.history(start=startDate,
                                     end=endDate))