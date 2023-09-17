# NSE (national stock exchange) data

Introduction:
This library serves as an api to fetch data from the NSE about stocks and indices and derivatives using python

Thank you for using Nsedt. Please feel free to send pull requests, comments, and suggestions, as well as get in touch with me if you require any additional help. I sincerely hope you will find this library useful.

## How to start
1. clone the repository
`git clone https://github.com/pratik141/nsedt`
2. Install the requirements file after changing to cloned folder above
`pip install -r requirements.txt`
3. Install locally 
`pip installl . --upgrade`

---
## Equity
### Details
|  Name | Module name | Description | Argument | Response|
| ----- | ----------- | ----------- | -------- | ------- |
| companyinfo | get_companyinfo | Company info | symbol , response_type | json, panda df |
| marketstatus | get_marketstatus | marketstatus | -- | panda_df |
| price | get_price | price | start_date, end_date, symbol, input_type | json, panda df |
| corpinfo | get_corpinfo | corpinfo | arg | |
| event | get_event | event | start_date, end_date |  panda df |
| chartdata | get_chartdata | chartdata | symbol | panda df |
| symbols_list | get_symbols_list | symbols_list | -- | json |

### step to run  
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
print(eq.get_symbols_list()) #print the list of symbols used by NSE for equities
```

## Indices
### Details
|  Name | Module name | Description | Argument | Response|
| ----- | ----------- | ----------- | -------- | ------- |
| price | get_price | price | start_date, end_date, symbol |  panda df |
### step to run  
```py

from nsedt import indices as ind
from datetime import date

start_date = date(2022, 1, 1)
end_date = date(2023, 1, 10)
print(ind.get_price(start_date=start_date, end_date=end_date, symbol="NIFTY 50"))
```

## Derivatives
### Details
|  Name | Module name | Description | Argument | Response|
| ----- | ----------- | ----------- | -------- | ------- |
| vix | get_vix | price | start_date, end_date,columns_drop_list |  panda df |
| option chain | get_option_chain | get option  price | symbol,strikePrice,expiryDate |  panda df |
| option chain expiry date | get_option_chain_expdate | option chain expiry date | symbol |  json  |
| future price | get_future_price | get future price | symbol, start_date, end_date, expiryDate,response_type, columns_drop_list |  panda df |
| future expiry date | get_future_expdate | future expiry date | symbol |  json  |


### step to run  
```py
from nsedt import derivatives as de
start_date = "01-09-2023"
end_date = "03-09-2023"
# date format "%d-%m-%Y"
print(de.get_vix(start_date, end_date))
print(de.get_option_chain(symbol="TCS", strikePrice=3300, expiryDate="expiryDate"))
print(de.get_option_chain_expdate(symbol="TCS"))
print(de.get_future_price(symbol="TCS", start_date=start_date, end_date=end_date))
print(de.get_future_expdate(symbol="TCS"))
