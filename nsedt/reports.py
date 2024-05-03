"""
function to download reports
"""

import logging

from nsedt.utils import get_cookies, fetch_csv, format_date
from nsedt.resources import constants as cns

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
    date = format_date(date, format='%d%m%y')
    if not date:
        raise ValueError("Please provide date format in '%d-%m-%Y' format")

    cookies = get_cookies()
    url = f"{cns.REPORT_URL}{cns.MARKET_ACTIVITY_REPORT}{date}.csv"
    return fetch_csv(url, cookies, response_type="raw")


def get_bhav_copy_zip(date: str, file_path: str):
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

    date = format_date(date, format='%d%b%Y')
    if not date:
        raise ValueError("Please provide date format in '%d-%m-%Y' format")

    cookies = get_cookies()
    url = f"{cns.REPORT_URL}{cns.BHAV_COPY_REPORT}{date[2:5]}/cm{date}bhav.csv.zip"
    content = fetch_csv(url, cookies, response_type="raw")
    file_path = file_path.removesuffix("/")
    try:
        with open(f"{file_path}/{date}bhav.csv.zip", 'wb') as f:
            f.write(content)
        return True
    except Exception as e:
        raise ValueError("Unable to download the bhavcopy zip") from e
    
