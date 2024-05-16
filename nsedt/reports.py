"""
function to download reports
"""

import logging

from io import BytesIO
import pandas as pd

from nsedt.utils import get_cookies, fetch_csv, format_date, fetch_zip
from nsedt.resources.constants import (
    REPORT_URL, MARKET_ACTIVITY_REPORT,
    BHAV_COPY_REPORT, SEC_BHAV_COPY_REPORT, NSCCL_REPORTS, NSCCL_VOLT)


log = logging.getLogger("root")

# tbd
# bulk deals
# block deals


def get_market_activity_report(date: str):
    """
    get_market_activity_report

    Args:\n
        date (str): date for which to download market activity report\n
    Returns:
        df = Returns dataframe for  market activity report for sectors
        for the given date
    Expects:
        date to be in format of  "dd-mm-yyyy" eg: 30-04-2024
        all other cases will be invalidated
    """
    date = format_date(date, date_format='%d%m%y')
    if not date:
        raise ValueError("Please provide date format in '%d-%m-%Y' format")

    cookies = get_cookies()
    url = f"{REPORT_URL}{MARKET_ACTIVITY_REPORT}{date}.csv"
    response = fetch_csv(url, cookies, response_type="raw")
    df = pd.read_csv(BytesIO(response), skiprows=8)
    df.drop(columns=['Unnamed: 0'], inplace=True)
    df = df[:77]
    return df

def get_volatility_report(date: str, response_type: str="panda_df"):
    """
    get_volatility_report

    Args:\n
        date (str): date for which to download market activity report\n
        response_type (str, Optional): define the response type panda_df | json . Default json\n
    Returns:
        string: string content of the file as right now its not possible
        to format the content to json or pandas df
    Expects:
        date to be in format of  "dd-mm-yyyy" eg: 30-04-2024
        all other cases will be invalidated
    """
    date = format_date(date, date_format='%d%m%Y')
    if not date:
        raise ValueError("Please provide date format in '%d-%m-%Y' format")
    cookies = get_cookies()
    url = f"{REPORT_URL}{NSCCL_VOLT}CMVOLT_{date}.CSV"
    print(url)
    return fetch_csv(url, cookies, response_type=response_type)


def get_bhav_copy_zip(date: str, response_type: str="panda_df"):
    """
    get_market_activity_report

    Args:\n
        date (str): date for which to download market activity report\n
        path (str): path to save the bhav copy zip
    Returns:
        bool: if the file is save to the local path or not
    Expects:
        date to be in format of  "dd-mm-yyyy" eg: 30-04-2024
    """

    date = format_date(date, date_format='%d%b%Y')
    if not date:
        raise ValueError("Please provide date format in '%d-%m-%Y' format")
    date = date.upper()
    cookies = get_cookies()
    url = f"{REPORT_URL}{BHAV_COPY_REPORT}{date[2:5]}/cm{date}bhav.csv.zip"
    file_name = url.split("/")[-1].replace(".zip", "")
    return fetch_zip(url, cookies, file_name=file_name, response_type=response_type)


def get_sec_full_bhav_copy(date: str, response_type: str="panda_df"):
    """
    get_sec_full_bhav_copy

    Args:\n
        date (str): date for which to download market activity report\n
        response_type (str, Optional): define the response type panda_df | json . Default json\n
    Returns:
        string: string content of the file as right now its not possible
        to format the content to json or pandas df
    Expects:
        date to be in format of  "dd-mm-yyyy" eg: 30-04-2024
        all other cases will be invalidated
    """
    date = format_date(date, date_format='%d%m%Y')
    if not date:
        raise ValueError("Please provide date format in '%d-%m-%Y' format")

    cookies = get_cookies()
    url = f"{REPORT_URL}{SEC_BHAV_COPY_REPORT}sec_bhavdata_full_{date}.csv"
    return fetch_csv(url, cookies, response_type=response_type)


def get_fno_participant_wise_oi_data(date: str, response_type: str="panda_df"):
    """
    fno_participant_wise_oi_data

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
    date = format_date(date, date_format='%d%m%Y')
    if not date:
        raise ValueError("Please provide date format in '%d-%m-%Y' format")

    cookies = get_cookies()
    url = f"{REPORT_URL}{NSCCL_REPORTS}fao_participant_oi_{date}.csv"
    return fetch_csv(url, cookies, response_type=response_type, skip_rows=1)


def get_fno_participant_wise_volume_data(date: str,response_type: str="panda_df"):
    """
    get_fno_participant_wise_volume_data

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
    date = format_date(date, date_format='%d%m%Y')
    if not date:
        raise ValueError("Please provide date format in '%d-%m-%Y' format")

    cookies = get_cookies()
    url = f"{REPORT_URL}{NSCCL_REPORTS}fao_participant_vol_{date}.csv"
    return fetch_csv(url, cookies, response_type=response_type, skip_rows=1)
