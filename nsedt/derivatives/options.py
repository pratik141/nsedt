""" 
get data for Options
"""
import logging
import urllib

from datetime import datetime
from nsedt import utils
from nsedt.resources import constants as cns
from nsedt.utils import data_format

log = logging.getLogger("root")


def get_option_chain(
    symbol: str,
    strike_price: str = None,
    expiry_date: str = None,
    response_type="panda_df",
):
    """Get option data of stock and indices

    Args:
        symbol (str): _description_
        strikePrice (str, optional): _description_. Defaults to None.
        expiryDate (str, optional): _description_. Defaults to None.
        response_type (str, optional): _description_. Defaults to "panda_df".
    Returns:
        Pandas DataFrame: df containing option data
      or
        Json: json containing option data

    """
    params = {}
    cookies = utils.get_cookies()
    base_url = cns.BASE_URL

    if symbol in cns.INDICES:
        event_api = cns.OPTIONS_PRICE_EQUITIES
    else:
        event_api = cns.OPTIONS_PRICE_EQUITIES

    params["symbol"] = symbol

    url = base_url + event_api + urllib.parse.urlencode(params)
    data = utils.fetch_url(url, cookies, response_type="json")

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
        list: expiry date in list(in "%d-%m-%Y" format)
    """
    params = {}
    cookies = utils.get_cookies()
    base_url = cns.BASE_URL

    if symbol in cns.INDICES:
        event_api = cns.OPTIONS_PRICE_EQUITIES
    else:
        event_api = cns.OPTIONS_PRICE_EQUITIES

    params["symbol"] = symbol

    url = base_url + event_api + urllib.parse.urlencode(params)
    data = utils.fetch_url(url, cookies, response_type="json")
    ret = []
    for expiry_date in data["records"]["expiryDates"]:
        ret.append(datetime.strptime(expiry_date, "%d-%b-%Y").strftime("%d-%m-%Y"))
    return ret
