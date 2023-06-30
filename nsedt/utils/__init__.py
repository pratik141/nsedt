"""
utils for nsedt
"""

import json

import pandas as pd
import requests
from nsedt.resources import constants as cns


def get_headers():
    """
    Args:
       ---
    Returns:
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
       cookies (str): NSE cokies
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
