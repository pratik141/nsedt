"""
  Test case for nsedt.indices
"""

from typing import List
import pandas as pd

from nsedt.derivatives import futures as fut

START_DATE = "01-01-2024"
END_DATE = "10-01-2024"
SYMBOL = "NIFTY"


def test_get_future_price():
    """
    Test the get_price function from nsedt.derivatives.futures module.
    """

    data = fut.get_future_price(
        start_date=START_DATE,
        end_date=END_DATE,
        expiry_date="25-01-2024",
        symbol=SYMBOL,
    )
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 8
    assert list(data.columns) == [
        "Expiry Date",
        "Open Price",
        "High Price",
        "Low Price",
        "Close Price",
        "FH_PREV_CLS",
        "FH_SETTLE_PRICE",
        "FH_TOT_TRADED_QTY",
        "FH_TOT_TRADED_VAL",
        "FH_OPEN_INT",
        "Change in OI",
        "Date",
        "FH_UNDERLYING_VALUE",
    ]


def test_get_future_expdate():
    """
    Test the get_future_expdate function from nsedt.derivatives.futures module.
    """
    data = fut.get_future_expdate(
        symbol=SYMBOL,
    )
    assert isinstance(data, List)
    assert len(data) == 3
