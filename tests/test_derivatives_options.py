"""
  Test case for nsedt.derivatives.options
"""

from typing import List

import pandas as pd

from nsedt.derivatives import options as opt

from nsedt import derivatives as de

START_DATE = "01-01-2024"
END_DATE = "10-01-2024"
SYMBOL = "TCS"


def test_get_option_chain():
    """
    Test the get_option_chain function from nsedt.derivatives.options module.
    """

    expiry_date = opt.get_option_chain_expdate(SYMBOL)[0]
    data = opt.get_option_chain(SYMBOL, expiry_date=expiry_date)
    assert isinstance(data, pd.DataFrame)
    assert len(data) > 10
    assert list(data.columns) == [
        "strikePrice",
        "expiryDate",
        "PE.underlying",
        "PE.openInterest",
        "PE.changeinOpenInterest",
        "PE.pchangeinOpenInterest",
        "PE.totalTradedVolume",
        "PE.impliedVolatility",
        "PE.lastPrice",
        "PE.change",
        "PE.pChange",
        "PE.totalBuyQuantity",
        "PE.totalSellQuantity",
        "PE.bidQty",
        "PE.bidprice",
        "PE.askQty",
        "PE.askPrice",
        "PE.underlyingValue",
        "CE.underlying",
        "CE.openInterest",
        "CE.changeinOpenInterest",
        "CE.pchangeinOpenInterest",
        "CE.totalTradedVolume",
        "CE.impliedVolatility",
        "CE.lastPrice",
        "CE.change",
        "CE.pChange",
        "CE.totalBuyQuantity",
        "CE.totalSellQuantity",
        "CE.bidQty",
        "CE.bidprice",
        "CE.askQty",
        "CE.askPrice",
        "CE.underlyingValue",
    ]
    assert data.loc[0, "PE.underlying"] == SYMBOL


def test_get_option_chain_expdate():
    """
    Test the get_option_chain_expdate function from nsedt.derivatives.options module.
    """

    data = opt.get_option_chain_expdate(SYMBOL)
    assert isinstance(data, List)
    assert len(data) > 1


def test_get_historical_option_data():
    """
    Test the get_historical_option_data function from nsedt.derivatives.options module.
    """
    data = opt.get_historical_option_data(
        symbol=SYMBOL,
        start_date=START_DATE,
        end_date=END_DATE,
        option_type="CE",
        strike_price="3300",
        year=2024,
        expiry_date="28-03-2024",
    )
    assert isinstance(data, pd.DataFrame)



def test_get_derivatives_symbols():
    """
    Test the get_derivatives_symbols function from nsedt.derivatives.options module.
    """
    data=de.get_derivatives_symbols()
    symList=[i['symbol'] for i in data['UnderlyingList']]
    assert isinstance(symList, List)
