from nsedt import derivatives as de

start_date = "24-04-2024"
end_date = "25-04-2024"
report_date = "11-06-2024"
report_past_date = "04-06-2024"
# date format "%d-%m-%Y"

symbol="FINNIFTY"

print(de.get_vix(start_date, end_date))
print(de.get_option_chain_expdate(symbol=symbol))
print(de.get_option_chain(symbol=symbol, strike_price=19200, expiry_date=report_date))
print(de.get_future_price(symbol=symbol, start_date=start_date, end_date=end_date))
print(de.get_future_expdate(symbol=symbol))
print(de.get_historical_option_data(symbol=symbol, start_date=start_date, end_date=end_date, option_type="CE", strike_price="22000", year="2024", expiry_date=report_past_date))