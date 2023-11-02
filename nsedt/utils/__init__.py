"""
utils for nsedt
"""

import json
import datetime
from warnings import warn
import pandas as pd
import requests
from nsedt.resources import constants as cns



def get_headers():
    """
    Args:
        ---\n
    Returns:\n
        Json: json containing nse header
    """

    return {
        "Host": "www.nseindia.com",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Requested-With": "XMLHttpRequest",
        "DNT": "1",
        "Connection": "keep-alive",
    }


def get_cookies():
    """
    Args:
        ---

    Returns:

        Json: json containing nse cookies
    """

    response = requests.get(cns.BASE_URL, timeout=30, headers=get_headers())
    if response.status_code != 200:
        raise ValueError("Retry again in a minute.")
    return response.cookies.get_dict()


def fetch_url(url, cookies, key=None, response_type="panda_df"):
    """
    Args:

        url (str): URL to fetch
        cookies (str): NSE cookies
        key (str, Optional):

    Returns:

        Pandas DataFrame: df containing url data

    """

    response = requests.get(
        url=url,
        timeout=30,
        headers=get_headers(),
        cookies=cookies,
    )

    if response.status_code == 200:
        json_response = json.loads(response.content)

        if response_type != "panda_df":
            return json_response
        if key is None:
            return pd.DataFrame.from_dict(json_response)

        return pd.DataFrame.from_dict(json_response[key])

    raise ValueError("Please try again in a minute.")


def get_symbol(symbol: str, get_key: str) -> str:
    """_summary_

    Args:
        symbol (str): _description_
        get_key (str): _description_

    Returns:
        str: _description_
    """

    symbol_map = cns.SYMBOL_MAP
    val = None
    for item in symbol_map:
        key_list = item["keys"]
        if symbol in key_list:
            val = item[get_key]

    return val if val else symbol


def check_nd_convert(start_date: str, end_date: str) -> datetime:
    """
    The function `check_nd_convert` takes two date strings in the format "%d-%m-%Y" and 
    converts them to datetime objects if they are not already in that format.

    :param start_date: The `start_date` parameter is the starting date of a period,
     specified as a string in the format "%d-%m-%Y"
    :type start_date: str
    :param end_date: The `end_date` parameter is a string representing the end date in the format
    "%d-%m-%Y"
    :type end_date: str
    :return: the start_date and end_date as datetime objects.
    """

    if isinstance(start_date, datetime.date) and isinstance(end_date, datetime.date):
        warn(
            """Passing start_date, end_date in date is deprecated
now pass in str '%d-%m-%Y' format""",
            DeprecationWarning,
            stacklevel=2,
        )

    elif isinstance(start_date, str) and isinstance(end_date, str):
        start_date = datetime.datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.datetime.strptime(end_date, "%d-%m-%Y")

    else:
        raise ValueError("Input is of an unknown type")

    return start_date, end_date
