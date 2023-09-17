""" 
get data for Options
"""
import logging
import urllib

from nsedt import utils
from nsedt.resources import constants as cns
from nsedt.utils import data_format

log = logging.getLogger("root")


def get_option_chain(
    symbol: str,
    strikePrice: str = None,
    expiryDate: str = None,
    response_type="panda_df",
):
    """_summary_

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
        event_api = cns.DERIVATIVES_PRICE_INDICES
    else:
        event_api = cns.DERIVATIVES_PRICE_EQUITIES

    params["symbol"] = symbol

    url = base_url + event_api + urllib.parse.urlencode(params)
    data = utils.fetch_url(url, cookies, response_type="json")

    # filtering data
    if strikePrice and expiryDate:
        filtered_data = [
            record
            for record in data["records"]["data"]
            if record["strikePrice"] == strikePrice
            and record["expiryDate"] == expiryDate
        ]

    elif strikePrice:
        filtered_data = [
            record
            for record in data["records"]["data"]
            if record["strikePrice"] == strikePrice
        ]
    elif expiryDate:
        filtered_data = [
            record
            for record in data["records"]["data"]
            if record["expiryDate"] == expiryDate
        ]
    else:
        filtered_data = data["records"]["data"]

    return data_format.option_chain(
        filtered_data,
        response_type=response_type,
    )


def get_option_chain_expdate(symbol: str) -> list:
    """_summary_

    Args:
        symbol (str): _description_

    Returns:
        list: _description_
    """
    params = {}
    cookies = utils.get_cookies()
    base_url = cns.BASE_URL

    if symbol in cns.INDICES:
        event_api = cns.DERIVATIVES_PRICE_INDICES
    else:
        event_api = cns.DERIVATIVES_PRICE_EQUITIES

    params["symbol"] = symbol

    url = base_url + event_api + urllib.parse.urlencode(params)
    data = utils.fetch_url(url, cookies, response_type="json")
    return data["records"]["expiryDates"]
