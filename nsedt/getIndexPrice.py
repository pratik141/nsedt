
from nsedt import indices as ind
from datetime import date
import pandas as pd

start_date = "01-05-2023"
end_date = "03-05-2023"

print(ind.get_price(start_date=start_date, end_date=end_date, symbol="FINNIFTY"))
data = ind.get_price(start_date=start_date, end_date=end_date, symbol="FINNIFTY")
# To change date format from '%d-%b-%Y' to '%Y-%m-%d'
data["Date"] = pd.to_datetime(data["Date"],format='%d-%b-%Y')