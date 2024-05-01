"""
  Test case for nsedt.indices
"""

import pandas as pd

from nsedt import indices as ind

START_DATE = "01-01-2024"
END_DATE = "10-01-2024"
SYMBOL = "NIFTY"


def test_get_price():
    """
    Test the get_price function from nsedt.equity module.
    """

    data = ind.get_price(start_date=START_DATE, end_date=END_DATE, symbol="NIFTY")
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 8
    assert list(data.columns) == [
        "Open Price",
        "High Price",
        "Close Price",
        "Low Price",
        "Date",
    ]
    assert data.loc[0, "Open Price"] == 21727.75
    assert data.loc[3, "Close Price"] == 21658.6
