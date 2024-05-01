import pandas as pd

from nsedt.nsedt import equity as eq
from typing import Dict, List

start_date = "01-01-2024"
end_date = "10-01-2024"
symbol = "TCS"

def test_get_price():
  """
  Test the get_price function from nsedt.equity module.
  """

  data = eq.get_price(start_date, end_date, symbol)

  # Assert expected data structure and content
  assert isinstance(data, pd.DataFrame)
  assert len(data) == 8
  assert list(data.columns) == [
            "Date",
            "Open Price",
            "High Price",
            "Low Price",
            "Close Price",
            "Prev Close Price",
            "Last Traded Price",
            "Total Traded Quantity",
            "Total Traded Value",
            "52 Week High Price",
            "52 Week Low Price",
            "VWAP",
            "Deliverable Volume",
            "Deliverable Percent",
            "Series",
        ]
  assert data.loc[0, "Open Price"] == 3790.0
  assert data.loc[3, "Close Price"] == 3666.8


def test_get_event():
  """
  Test the get_event function from nsedt.equity module.
  """

  data = eq.get_event(start_date, end_date)

  # Assert expected data structure and content
  assert isinstance(data, pd.DataFrame)
  assert len(data) == 39
  assert list(data.columns) == ['symbol', 'company', 'purpose', 'bm_desc', 'date']
  assert data.loc[0, "company"] == 'Gensol Engineering Limited'
  assert data.loc[3, "date"] == '03-Jan-2024'


def test_get_companyinfo():
  """
  Test the get_companyinfo function from nsedt.equity module.
  """

  data = eq.get_companyinfo(symbol=symbol,response_type="json")

  # Assert expected data structure and content
  assert isinstance(data, Dict)
  assert len(data) == 7
  assert list(data.keys()) == ['info', 'metadata', 'securityInfo', 'sddDetails', 'priceInfo', 'industryInfo', 'preOpenMarket']
  assert data['info']['companyName'] == 'Tata Consultancy Services Limited'
  assert data['industryInfo']['sector'] == 'Information Technology'


def test_get_symbols_list():
  """
  Test the get_symbols_list function from nsedt.equity module.
  """

  data = eq.get_symbols_list()

  # Assert expected data structure and content
  assert isinstance(data, List)
  assert len(data) > 1000
  assert symbol in data


def test_get_asm_list():
  """
  Test the get_asm_list function from nsedt.equity module.
  """

  data = eq.get_asm_list(asm_type = "shortterm")

  # Assert expected data structure and content
  assert isinstance(data, List)
  assert len(data) > 1


def test_get_chartdatat():
  """
  Test the get_chartdata function from nsedt.equity module.
  """

  data = eq.get_chartdata(symbol="TCS")

  # Assert expected data structure and content
  assert isinstance(data, pd.DataFrame)
  assert len(data) > 1
  assert list(data.columns) == ['timestamp_milliseconds', 'price', 'datetime']
