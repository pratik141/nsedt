"""
utils for nsedt
"""

import io
import json
import datetime
import zipfile

from io import BytesIO

from datetime import datetime, date
from warnings import warn

import requests

import pandas as pd

from fake_http_header import FakeHttpHeader
from nsedt.resources import constants as cns



def format_df(df):
    """
    Arg:\n
        - df: pandas df
    Reuturn:
        - formatted df column 
    """
    df.columns = df.columns.str.lower().str.replace(' ','_').str.replace('\t','')
    return df

def format_date(input_string: str, date_format: str):
    """
    Args:\n
        - input_string : str date format for a format to check
        - format : type of string to format
    Returns:\n
        - str: date format in input string
    """
    try:
        return datetime.strptime(input_string, "%d-%m-%Y").strftime(date_format)
    except ValueError:
        return None


def get_headers():
    """
    Args:
        ---\n
    Returns:\n
        Json: json containing nse header
    """

    return FakeHttpHeader().as_header_dict()


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

    return val or symbol


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

    if isinstance(start_date, date) and isinstance(end_date, date):
        warn(
            """Passing start_date, end_date in date is deprecated
now pass in str '%d-%m-%Y' format""",
            DeprecationWarning,
            stacklevel=2,
        )

    elif isinstance(start_date, str) and isinstance(end_date, str):
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")

    else:
        raise ValueError("Input is of an unknown type")

    return start_date, end_date


def fetch_csv(url, cookies, response_type="panda_df", skip_rows=None):
    """
    Args:

        url (str): URL to fetch
        cookies (str): NSE cookies
        key (str, Optional):

    Returns:

        Pandas DataFrame: df generated from csv
        OR
        Json: json output of the csv
        OR
        String: raw content for files where it cannot be processed into Json or 
                Pandas df

    """

    response = requests.get(
        url=url, timeout=30, headers=get_headers(), cookies=cookies )
    if response.status_code == 200:
        if response_type == "raw":
            return response.content
        csv_content = response.content.decode('utf-8')
        df = pd.read_csv(io.StringIO(csv_content), skiprows=skip_rows)
        df = format_df(df)
        return df.to_json(orient='records') if response_type == "json" else df
    raise ValueError("Please try again in a minute.")


def fetch_zip(url, cookies, file_name, response_type="panda_df", skip_rows=None):
    """
    Args:

        url (str): URL to fetch
        cookies (str): NSE cookies
        key (str, Optional):
    Returns:

        Pandas DataFrame: df generated from csv
        OR
        Json: json output of the csv
        OR
        Pandas DF:  Pandas df of the csv file
    """

    if not file_name:
        raise ValueError("Please give file name to return")

    response = requests.get(
        url=url, timeout=30, headers=get_headers(), cookies=cookies )
    if response.status_code == 200:
        zip_content = BytesIO(response.content)
        # Open the zip file in memory
        with zipfile.ZipFile(zip_content, 'r') as zip_ref:
            # Retrieve the list of file names in the zip file
            try:
                csv_content = zip_ref.read(file_name)
            except Exception as e:
                raise ValueError("File not found in the zip folder.") from e

            df = pd.read_csv(BytesIO(csv_content), skiprows=skip_rows)
            df = format_df(df)
            return df.to_json(orient='records') if response_type == "json" else df
    raise ValueError("File might not be available this time or check your params")
