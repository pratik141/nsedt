import datetime
import concurrent
from concurrent.futures import ALL_COMPLETED
import pandas as pd
from nsedt import utils
from nsedt.utils import data_format
import urllib
from nsedt.resources import constants as cns
import logging

logging.basicConfig(
    level=logging.INFO,
    format=cns.log_format,
    datefmt="%m/%d/%Y %I:%M:%S %p",
)


def get_price(start_date, end_date, symbol=None, input_type="stock"):
    """
    Create threads for different requests, parses data, combines them and returns dataframe
    Args:
        start_date (datetime.datetime): start date
        end_date (datetime.datetime): end date
        input_type (str): Either 'stock' or 'index'
        symbol (str, optional): stock symbol. Defaults to None. TODO: implement for index`
    Returns:
        Pandas DataFrame: df containing data for symbol of provided date range
    """
    cookies = utils.get_cookies()
    base_url = cns.base_url
    price_api = cns.equity_price_histroy
    url_list = []

    # set the window size to one year
    window_size = datetime.timedelta(days=cns.window_size)

    current_window_start = start_date
    while current_window_start < end_date:
        current_window_end = current_window_start + window_size

        # check if the current window extends beyond the end_date
        if current_window_end > end_date:
            current_window_end = end_date

        st = current_window_start.strftime("%d-%m-%Y")
        et = current_window_end.strftime("%d-%m-%Y")

        if input_type == "stock":
            params = {
                "symbol": symbol,
                "from": st,
                "to": et,
                "dataType": "priceVolumeDeliverable",
                "series": "EQ",
            }
            url = base_url + price_api + urllib.parse.urlencode(params)
            url_list.append(url)

        # move the window start to the next day after the current window end
        current_window_start = current_window_end + datetime.timedelta(days=1)

    result = pd.DataFrame()
    with concurrent.futures.ThreadPoolExecutor(max_workers=cns.max_workers) as executor:
        future_to_url = {
            executor.submit(utils.fetch_url, url, cookies): url for url in url_list
        }
        concurrent.futures.wait(future_to_url, return_when=ALL_COMPLETED)
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                df = future.result()
                result = pd.concat([result, df])
            except Exception as exc:
                logging.error(f"{url} got exception: {exc}. Please try again later.")
                raise exc
    return data_format.price(result)


def get_corpinfo(start_date, end_date, symbol=None):
    """
    Create threads for different requests, parses data, combines them and returns dataframe
    Args:
        start_date (datetime.datetime): start date
        end_date (datetime.datetime): end date
        symbol (str, optional): stock symbol. Defaults to None. TODO: implement for index`
    Returns:
        Pandas DataFrame: df containing data for symbol of provided date range
    """
    cookies = utils.get_cookies()
    params = {
        "symbol": symbol,
        "from_date": start_date,
        "to_date": end_date,
        "index": "equities",
    }
    base_url = cns.base_url
    price_api = cns.equity_corpinfo
    url = base_url + price_api + urllib.parse.urlencode(params)
    return utils.fetch_url(url, cookies)
