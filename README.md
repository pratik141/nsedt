# nse data

Introduction

Thank you for using Nsedt. Please feel free to send pull requests, comments, and suggestions, as well as get in touch with me if you require any additional help. I sincerely hope you will find this library useful.

---
## Run 
```py
from nsedt import equity as eq
from datetime import date

start_date = date(2022, 1, 1)
end_date = date(2023, 1, 10)
print(eq.get_price(start_date, end_date, symbol="TCS"))
start_date = "01-05-2023"
end_date = "03-05-2023"
print(eq.get_corpinfo(start_date, end_date, symbol="TCS"))
print(eq.get_event(start_date, end_date))
print(eq.get_event())
print(eq.get_marketstatus())
print(eq.get_marketstatus(response_type="json"))
print(eq.get_companyinfo(symbol="TCS"))
print(eq.get_companyinfo(symbol="TCS", response_type="json"))
print(eq.get_chartdata(symbol="TCS"))

```
---
## Output
```sh
# get_price
        Date  Open Price  High Price  Low Price  Close Price  ...  52 Week High Price  52 Week Low Price     VWAP  Deliverable Volume  Deliverable Percent
0   2022-01-03      3750.0     3830.00    3745.00      3817.75  ...              3989.9             2880.0  3807.43             1433211                61.09
..         ...         ...         ...        ...          ...  ...                 ...                ...      ...                 ...                  ...
104 2023-01-04      3306.7     3327.35    3286.20      3314.65  ...              4043.0             2926.1  3306.45              778260                63.19

# get_corpinfo
symbol series ind faceVal                                            subject  ... ndStartDate                               comp          isin ndEndDate caBroadcastDate
0    TCS     EQ   -       1                         Dividend - Rs 22 Per Share  ...           -  Tata Consultancy Services Limited  INE467B01029         -            None
3    TCS     EQ   -       1  Interim Dividend - Rs 8 Per Share Special Divi...  ...           -  Tata Consultancy Services Limited  INE467B01029         -            None

# get_event
        symbol                                   company  ...                                            bm_desc         date
0       5PAISA                    5Paisa Capital Limited  ...  To consider and approve the financial results ...  01-May-2023
56  ANTGRAPHIC                        Antarctica Limited  ...  Antarctica Limited has informed the Exchange t...  03-May-2023

#get_companyinfo
                                               info                           metadata securityInfo  ... priceInfo   industryInfo preOpenMarket
symbol                                           TCS                                TCS          NaN  ...       NaN            NaN           NaN
atoSellQty                                       NaN                                NaN          NaN  ...       NaN            NaN           491

#get_companyinfo json format
{"info":{"symbol":"TCS","companyName":"Tata Consultancy Services Limited","industry":"COMPUTERS - SOFTWARE","activeSeries":["EQ"],"debtSeries":[],"tempSuspendedSeries":[],"isFNOSec":true,"isCASec":false,"isSLBSec":true,"isDebtSec":false,"isSuspended":false,"isETFSec":false,"isDelisted":false, ......}

#get_marketstatus

           market marketStatus     tradeDate     index     last  ... percentChange marketStatusMessage   expiryDate underlying tradeDateFormatted
0  Capital Market        Close   09-Jun-2023  NIFTY 50  18563.4  ...         -0.38    Market is Closed          NaN        NaN                NaN
4  currencyfuture        Close  Invalid date            82.4975  ...                  Market is Closed  16-Jun-2023     USDINR        09-Jun-2023


#get_chartdata
                 0        1
0    1686301201000  3300.00
404  1686301620000  3250.00


```
---

# API Documentation

## Functions

### get_companyinfo

Function description goes here.

### get_marketstatus

Function description goes here.

### get_price

Function description goes here.

### get_corpinfo

Function description goes here.

### get_event

Function description goes here.

### get_chartdata

Function description goes here.

