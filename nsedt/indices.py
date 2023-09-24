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
    start_date,
    end_date,
    symbol,
    response_type="panda_df",
    columns_drop_list: list = None,
    columns_rename_map: map = None,
):
    """_summary_

    Args:
        start_date (_type_): _description_
        end_date (_type_): _description_
        symbol (_type_): _description_
        response_type (str, optional): _description_. Defaults to "panda_df".

    Raises:
        exc: _description_

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
