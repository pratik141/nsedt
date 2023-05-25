import json
import pandas as pd
import requests
from nsedt.resources import constants as cns

base_url = cns.base_url


def get_headers():
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
    response = requests.get(base_url, timeout=30, headers=get_headers())
    if response.status_code != requests.codes.ok:
        raise ValueError("Retry again in a minute.")
    return response.cookies.get_dict()


def fetch_url(url, cookies):
    response = requests.get(url, timeout=30, headers=get_headers(), cookies=cookies)
    if response.status_code == requests.codes.ok:
        json_response = json.loads(response.content)
        try:
            return pd.DataFrame.from_dict(json_response["data"])
        except:
            return pd.DataFrame.from_dict(json_response)
    else:
        raise ValueError("Please try again in a minute.")
