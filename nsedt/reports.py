"""
function to download reports
"""

import logging

from nsedt.utils import get_cookies, fetch_csv, format_date, fetch_zip
from nsedt.resources.constants import (
    REPORT_URL, MARKET_ACTIVITY_REPORT, BHAV_COPY_REPORT)

log = logging.getLogger("root")


def get_market_activity_report(date: str):
    """
    get_market_activity_report

    Args:\n
        date (str): date for which to download market activity report\n
        response_type (str, Optional): define the response type panda_df | json . Default json\n
    Returns:
        string: string content of the file as right now its not possible 
        to format the content to json or pandas df
    Expects: 
        date to be in format of  "ddmmYY" eg: 30/04/2024 => 300424
        all other cases will be invalidated
    """
    date = format_date(date, date_format='%d%m%y')
    if not date:
        raise ValueError("Please provide date format in '%d-%m-%Y' format")

    cookies = get_cookies()
    url = f"{REPORT_URL}{MARKET_ACTIVITY_REPORT}{date}.csv"
    return fetch_csv(url, cookies, response_type="raw")


def get_bhav_copy_zip(date: str, response_type: str="panda_df"):
    """
    get_market_activity_report

    Args:\n
        date (str): date for which to download market activity report\n
        path (str): path to save the bhav copy zip
    Returns:
        bool: if the file is save to the local path or not
    Expects: 
        date to be in format of  "ddmmYY" eg: 30/04/2024 => 30APR2024
        all other cases will be invalidated
    """

    date = format_date(date, date_format='%d%b%Y')
    if not date:
        raise ValueError("Please provide date format in '%d-%m-%Y' format")
    date = date.upper()
    cookies = get_cookies()
    url = f"{REPORT_URL}{BHAV_COPY_REPORT}{date[2:5]}/cm{date}bhav.csv.zip"
    file_name = url.split("/")[-1].replace(".zip", "")
    return fetch_zip(url, cookies, file_name=file_name, response_type=response_type)
