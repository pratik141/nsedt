# NSE (national stock exchange) data

Introduction:
This library serves as an api to fetch data from the NSE about stocks and indices and derivatives using python

Thank you for using Nsedt. Please feel free to send pull requests, comments, and suggestions, as well as get in touch with me if you require any additional help. I sincerely hope you will find this library useful.

#### For detailed doc please refer [nse-doc](https://pratikanand.co.in/nsedt/html)

## How to start

1. clone the repository
   `git clone https://github.com/pratik141/nsedt`
2. Install the requirements file after changing to cloned folder above
   `pip install -r requirements.txt`
3. Install locally
   `pip install . --upgrade`

---

## Equity

### Details

| Name         | Module name      | Description  | Argument                                 | Response       |
| ------------ | ---------------- | ------------ | ---------------------------------------- | -------------- |
| companyinfo  | get_companyinfo  | Company info | symbol , response_type                   | json, panda df |
| marketstatus | get_marketstatus | marketstatus | --                                       | panda_df       |
| price        | get_price        | price        | start_date, end_date, symbol, input_type | json, panda df |
| corpinfo     | get_corpinfo     | corpinfo     | arg                                      |                |
| event        | get_event        | event        | start_date, end_date                     | panda df       |
| chartdata    | get_chartdata    | chartdata    | symbol                                   | panda df       |
| symbols_list | get_symbols_list | symbols_list | --                                       | json           |
| asm_list     | get_asm_list     | symbols_list | asm_type                                 | json           |

Now get_price work with start_date, end_date without datetime format it support `%d-%m-%Y`

### step to run

```py
from nsedt import equity as eq
from datetime import date
start_date = "01-05-2023"
end_date = "03-05-2023"

print(eq.get_price(start_date, end_date, symbol="TCS"))
print(eq.get_corpinfo(start_date, end_date, symbol="TCS"))
print(eq.get_event(start_date, end_date))
print(eq.get_event())
print(eq.get_marketstatus())
print(eq.get_marketstatus(response_type="json"))
print(eq.get_companyinfo(symbol="TCS"))
print(eq.get_companyinfo(symbol="TCS", response_type="json"))
print(eq.get_chartdata(symbol="TCS"))
print(eq.get_symbols_list()) #print the list of symbols used by NSE for equities
print(eq.get_asm_list(asm_type = "shortterm"))
```

## Indices

### Details

| Name  | Module name | Description | Argument                     | Response |
| ----- | ----------- | ----------- | ---------------------------- | -------- |
| price | get_price   | price       | start_date, end_date, symbol | panda df |

### step to run

```py

from nsedt import indices as ind
from datetime import date
start_date = "01-05-2023"
end_date = "03-05-2023"

print(ind.get_price(start_date=start_date, end_date=end_date, symbol="NIFTY 50"))
data = ind.get_price(start_date=start_date, end_date=end_date, symbol="NIFTY")
# To change date format from '%d-%b-%Y' to '%Y-%m-%d'
data["Date"] = pd.to_datetime(data["Date"],format='%d-%b-%Y')
```

## Derivatives

### Details

| Name                     | Module name                | Description                                          | Argument                                                                  | Response        |
| ------------------------ | -------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------- | --------------- |
| vix                      | get_vix                    | price                                                | start_date, end_date,columns_drop_list                                    | panda df        |
| option chain             | get_option_chain           | get option price                                     | symbol,strikePrice,expiryDate                                             | panda df        |
| option chain expiry date | get_option_chain_expdate   | option chain expiry date                             | symbol                                                                    | json            |
| future price             | get_future_price           | get future price                                     | symbol, start_date, end_date, expiryDate,response_type, columns_drop_list | panda df        |
| future expiry date       | get_future_expdate         | future expiry date                                   | symbol                                                                    | json            |
| historical option chain  | get_historical_option_data | get historical option value for a given strike price | symbol, start_date,end_date,option_type,strike_price,year,expiry_date     | json, pandas df |

### step to run

```py
from nsedt import derivatives as de
start_date = "24-04-2024"
end_date = "25-04-2024"
# date format "%d-%m-%Y"

print(de.get_vix(start_date, end_date))
print(de.get_option_chain_expdate(symbol="TCS"))
print(de.get_option_chain(symbol="TCS", strike_price=3300, expiry_date=report_date))
print(de.get_future_price(symbol="TCS", start_date=start_date, end_date=end_date))
print(de.get_future_expdate(symbol="TCS"))
print(de.get_historical_option_data(symbol="TATAMOTORS", start_date=start_date, end_date=end_date, option_type="CE", strike_price="1020", year="2024", expiry_date="30-May-2024"))
print(de.get_derivatives_symbols())

```


# Reports

### Details

Note: Not all reports will be available for a given date, some reports are only available for a given date
and some for 2-3 weeks.

| Name                             | Module name                          | Description                                 | Argument            | Response          |
| -------------------------------- | ------------------------------------ | ------------------------------------------- | ------------------- | ----------------- |
| market activity                  | get_market_activity_report           | get raw text of market activity report      | date                | string            |
| bhav copy                        | get_bhav_copy_zip                    | download bhav copy zip for a given day      | date, response_type | json or pandas df |
| sec full bhav copy               | get_sec_full_bhav_copy               | download full bhav copy zip for a given day | date, response_type | json or pandas df |
| volatitly report                 | get_volatility_report                | download volatility report for a given day  | date, response_type | json or pandas df |
| fno participant wise oi data     | get_fno_participant_wise_oi_data     | fno participant oi data for a given day     | date, response_type | json or pandas df |
| fno participant wise volume data | get_fno_participant_wise_volume_data | fno participant volume data for a given day | date, response_type | json or pandas df |

### step to run

```py
from nsedt import reports as rep
report_date = "02-05-2024"
# date format "%d-%m-%Y"

print(rep.get_market_activity_report(date=report_date))
print(rep.get_bhav_copy_zip(date=report_date, response_type="json"))
print(rep.get_sec_full_bhav_copy(date=report_date, response_type="json"))
print(rep.get_volatility_report(date=report_date, response_type="json"))
print(rep.get_fno_participant_wise_oi_data(date=report_date, response_type="json"))
print(rep.get_fno_participant_wise_volume_data(date=report_date, response_type="json"))
```

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/pratik.anand)
