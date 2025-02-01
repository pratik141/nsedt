""" 
get data for Options
"""
import logging
import urllib

from datetime import datetime
from nsedt import utils
from nsedt.resources import constants as cns
from nsedt.utils import data_format, exceptions

log = logging.getLogger("root")


def get_derivatives_symbols():
    """
    Args:\n
        No arguments needed\n
    Returns:\n
        List of stock or equity symbols\n
    """
    cookies = utils.get_cookies()
    base_url = cns.BASE_URL
    event_api = cns.UNDERLYINF_INFO

    url = base_url + event_api
    data = utils.fetch_url(url, cookies)
    f_dict = data.to_dict()

    return f_dict["data"]


def get_option_chain(
    symbol: str,
    strike_price: str = None,
    expiry_date: str = None,
    response_type="panda_df",
):
    """Get option data of stock and indices

    Args:
        symbol (str): symbol name
        strike_price (str, optional): strike price to apply filter on price. Defaults to None.
        expiry_date (str, optional): expiry date to apply filter on date. Defaults to None.
        response_type (str, optional): response_type panda_df or json . Defaults to "panda_df".

    Returns:
        Pandas DataFrame: df containing option data
    or
        Json: json containing option data

    """
    params = {}
    cookies = utils.get_cookies()
    base_url = cns.BASE_URL
    symbol = utils.get_symbol(symbol=symbol, get_key="derivatives")

    if symbol in cns.INDICES:
        event_api = cns.OPTIONS_PRICE_INDICES
    else:
        event_api = cns.OPTIONS_PRICE_EQUITIES

    params["symbol"] = symbol

    url = base_url + event_api + urllib.parse.urlencode(params)
    data = utils.fetch_url(url, cookies, response_type="json")

    if data is None or data == {}:
        log.error("symbol is wrong or unable to access API")
        raise ValueError

    # filtering data

    if strike_price and expiry_date:
        filtered_data = [
            record
            for record in data["records"]["data"]
            if record["strikePrice"] == strike_price
            and record["expiryDate"]
            == datetime.strptime(expiry_date, "%d-%m-%Y").strftime("%d-%b-%Y")
        ]

    elif strike_price:
        filtered_data = [
            record
            for record in data["records"]["data"]
            if record["strikePrice"] == strike_price
        ]
    elif expiry_date:
        filtered_data = [
            record
            for record in data["records"]["data"]
            if record["expiryDate"]
            == datetime.strptime(expiry_date, "%d-%m-%Y").strftime("%d-%b-%Y")
        ]
    else:
        filtered_data = data["records"]["data"]

    return data_format.option_chain(
        filtered_data,
        response_type=response_type,
    )


def get_option_chain_expdate(symbol: str) -> list:
    """get option  expiry date for stock and indices

    Args:
        symbol (str): symbol name

    Returns:
        list: expiry date in list("%d-%m-%Y" format)
    """
    params = {}
    cookies = utils.get_cookies()
    base_url = cns.BASE_URL

    if symbol in cns.INDICES:
        event_api = cns.OPTIONS_PRICE_INDICES
    else:
        event_api = cns.OPTIONS_PRICE_EQUITIES

    params["symbol"] = symbol

    url = base_url + event_api + urllib.parse.urlencode(params)
    data = utils.fetch_url(url, cookies, response_type="json")
    ret = []
    expiry_dates = data.get("records").get("expiryDates")
    if expiry_dates is None:
        log.error("expiry_dates is None, symbol is wrong or unable to access API")
        return []
    for expiry_date in expiry_dates:
        ret.append(datetime.strptime(expiry_date, "%d-%b-%Y").strftime("%d-%m-%Y"))
    return ret

def get_historical_option_data(
    symbol: str,
    start_date: str,
    end_date: str,
    option_type: str,
    strike_price: str,
    year : str,
    expiry_date: str,
    response_type: str = "panda_df",
    columns_drop_list: list = None,
):
    """
    Get historical data for option chain for a given expiry
    Args:
        symbol (str): valid scrip name
        start_date (str): in %d-%m-%Y format
        end_date (str): in %d-%m-%Y format
        option_type (str): CE or PE.
        strike_price (str): valid integer.
        year (str): in %Y format eg 2024.
        expiry_date (str): in %d-%m-%Y format
        response_type (str, optional): either json or pand_df. Defaults to "panda_df".
        columns_drop_list (list, optional): list of columns to skip. Defaults to None.

    Returns:
        _type_: either json or pandas df. Defaults to pandas_df
    """
    cookies = utils.get_cookies()
    base_url = cns.BASE_URL
    event_api = cns.FNO_HISTORY
    symbol = utils.get_symbol(symbol=symbol, get_key="derivatives")

    if option_type not in ["CE", "PE"]:
        raise ValueError("Option type must be either CE or PE")

    try:
        expiry_date = datetime.strptime(expiry_date, "%d-%m-%Y").strftime("%d-%b-%Y")
    except Exception as e:
        raise ValueError("Please give expiry date in %d-%b-%Y format") from e

    params = {
        "symbol": symbol,
        "from": start_date,
        "to": end_date,
        "instrumentType": "OPTSTK",
        "optionType": option_type,
        "expiryDate": expiry_date,
        "strikePrice": strike_price,
        "year": year,
    }
    url = base_url + event_api + urllib.parse.urlencode(params)
    data = utils.fetch_url(url, cookies, response_type="json")

    if data["data"] == []:
        raise exceptions.DateStrikePriceOutofRange()

    return data_format.derivaties_options(
        data,
        response_type=response_type, columns_drop_list=columns_drop_list,
    )
