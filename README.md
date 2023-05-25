# nse data

---
## Run 
```py
from nsedt import equity as eq
from datetime import date

start_date = date(2022, 1, 1)
end_date = date(2023, 1, 10)
print(eq.get_price(start_date, end_date, symbol="TCS"))
start_date = "01-03-2022"
end_date = "03-05-2023"
print(eq.get_corpinfo(start_date, end_date, symbol="TCS"))

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
```
