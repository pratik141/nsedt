""" 
get data for Futures
"""
import urllib
from datetime import datetime, timedelta

from nsedt import utils
from nsedt.resources import constants as cns
from nsedt.utils import data_format


def get_future_price(
    symbol: str,
    start_date: str,
    end_date: str,
    expiry_date: str = None,
    response_type: str = "panda_df",
    columns_drop_list: list = None,
):
    """
        get future price of stock / indices
    Args:
        symbol (str): _description_
        start_date (str): _description_
        end_date (str): _description_
        expiry_date (str, optional): _description_. Defaults to None.
        response_type (str, optional): _description_. Defaults to "panda_df".
        columns_drop_list (list, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    cookies = utils.get_cookies()
    base_url = cns.BASE_URL
    event_api = cns.FUTURES_PRICE
    params = {
        "symbol": symbol,
        "from": start_date,
        "to": end_date,
    }
    if symbol in cns.INDICES:
        params["instrumentType"] = "FUTIDX"
    else:
        params["instrumentType"] = "FUTSTK"

    url = base_url + event_api + urllib.parse.urlencode(params)
    data = utils.fetch_url(url, cookies, response_type="json")

    if expiry_date:
        filtered_data = [
            record
            for record in data["data"]
            if record["FH_EXPIRY_DT"]
            == datetime.strptime(expiry_date, "%d-%m-%Y").strftime("%d-%b-%Y")
        ]
    else:
        filtered_data = data["data"]

    return data_format.derivatives_futures(
        filtered_data,
        response_type=response_type,
        columns_drop_list=columns_drop_list,
    )


def get_future_expdate(symbol: str) -> list:
    """get expiry dates of futures

    Args:
        symbol (str): symbol name

    Returns:
        list: expiry dates
    """
    cookies = utils.get_cookies()
    base_url = cns.BASE_URL
    event_api = cns.FUTURES_PRICE
    params = {
        "symbol": symbol,
        "from": (datetime.now() - timedelta(days=3)).strftime("%d-%m-%Y"),
        "to": datetime.now().strftime("%d-%m-%Y"),
    }
    if symbol in cns.INDICES:
        params["instrumentType"] = "FUTIDX"
    else:
        params["instrumentType"] = "FUTSTK"

    url = base_url + event_api + urllib.parse.urlencode(params)
    data = utils.fetch_url(url, cookies, response_type="json")
    ret = []
    for rec in data["data"]:
        ret.append(
            datetime.strptime(rec["FH_EXPIRY_DT"], "%d-%b-%Y").strftime("%d-%m-%Y")
        )
    return list(set(ret))
