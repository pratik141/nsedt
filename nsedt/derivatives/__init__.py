from .options import *

""" 
get data for Equity
"""
import concurrent
from datetime import datetime, timedelta
import logging
import urllib
from concurrent.futures import ALL_COMPLETED

import pandas as pd

from nsedt import utils
from nsedt.resources import constants as cns
from nsedt.utils import data_format

log = logging.getLogger("root")


def get_vix(
    start_date: str,
    end_date: str,
    response_type: str = "panda_df",
):
    """_summary_

    Args:
        start_date (str): start date in "%d-%m-%Y" format
        end_date (str): end_date in "%d-%m-%Y" format
        response_type (str, optional): response_type. Defaults to "panda_df".

    Raises:
        exc: genral Exception

    Returns:
        Pandas DataFrame: df containing option data
      or
        Json: json containing option data

    """
    cookies = utils.get_cookies()
    params = {
        "from": start_date,
        "to": end_date,
    }
    base_url = cns.BASE_URL
    event_api = cns.VIX_HISTORY
    url_list = []
    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    end_date = datetime.strptime(end_date, "%d-%m-%Y")

    # set the window size to one year
    window_size = timedelta(days=cns.WINDOW_SIZE)

    current_window_start = start_date
    while current_window_start < end_date:
        current_window_end = current_window_start + window_size

        # check if the current window extends beyond the end_date
        current_window_end = min(current_window_end, end_date)

        params = {
            "from": current_window_start.strftime("%d-%m-%Y"),
            "to": current_window_end.strftime("%d-%m-%Y"),
        }
        url = base_url + event_api + urllib.parse.urlencode(params)
        url_list.append(url)

        # move the window start to the next day after the current window end
        current_window_start = current_window_end + timedelta(days=1)
    print(url_list)

    result = pd.DataFrame()
    with concurrent.futures.ThreadPoolExecutor(max_workers=cns.MAX_WORKERS) as executor:
        future_to_url = {
            executor.submit(utils.fetch_url, url, cookies, response_type="panda"): url
            for url in url_list
        }
        concurrent.futures.wait(future_to_url, return_when=ALL_COMPLETED)
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                dataframe = data_format.get_vix(future.result())
                result = pd.concat([result, dataframe])
            except Exception as exc:
                log.error("%s got exception: %s. Please try again later.", url, exc)
                raise exc

    if response_type == "panda_df":
        return result
    return result.to_json(orient="records")
