""" 
get data for indices
"""
import concurrent
import datetime
import logging
import urllib
from concurrent.futures import ALL_COMPLETED

import pandas as pd

from nsedt import utils
from nsedt.resources import constants as cns
from nsedt.utils import data_format

log = logging.getLogger("root")


def get_price(
    start_date: datetime,
    end_date: datetime,
    symbol: str,
    response_type: str = "panda_df",
    columns_drop_list: list = None,
    columns_rename_map: map = None,
):
    """
        Get price of index

    Args:

        start_date (datetime): start date
        end_date (datetime): end date
        symbol (str): symbol name or index name
        response_type (str, optional):  Define return type: panda_df or json.
                                        Defaults to "panda_df".
        columns_drop_list (list,optional): define columns drop list, Defaults to None
        columns_rename_map (map, optional): define columns rename map, Defaults to None

    Raises:

        exc: general Exception

    Returns:

            Pandas DataFrame: df containing company info
        or
            Json: json containing company info

    """
    params = {}
    cookies = utils.get_cookies()
    base_url = cns.BASE_URL
    event_api = cns.INDEX_PRICE_HISTORY
    symbol = utils.get_symbol(symbol=symbol, get_key="indices")

    url_list = []

    # set the window size to one year
    window_size = datetime.timedelta(days=cns.WINDOW_SIZE)
    start_date, end_date = utils.check_nd_convert(start_date, end_date)

    current_window_start = start_date
    while current_window_start < end_date:
        current_window_end = current_window_start + window_size

        # check if the current window extends beyond the end_date
        current_window_end = min(current_window_end, end_date)

        params = {
            "indexType": symbol,
            "from": current_window_start.strftime("%d-%m-%Y"),
            "to": current_window_end.strftime("%d-%m-%Y"),
        }
        url = base_url + event_api + urllib.parse.urlencode(params)
        url_list.append(url)

        # move the window start to the next day after the current window end
        current_window_start = current_window_end + datetime.timedelta(days=1)

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
                data = future.result()
                if (
                    data.get("data").get("indexCloseOnlineRecords") == []
                    or data.get("data").get("indexTurnoverRecords") == []
                ):
                    continue
                dataframe = data_format.indices(
                    data, columns_drop_list, columns_rename_map
                )
                result = pd.concat([result, dataframe])
            except Exception as exc:
                log.error("%s got exception: %s. Please try again later.", url, exc)
                raise exc

    if response_type == "panda_df":
        return result
    return result.to_json(orient="records")
