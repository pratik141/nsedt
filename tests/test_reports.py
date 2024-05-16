"""
  Test case for nsedt.reports
"""

import pandas as pd
from nsedt.reports import (
    get_bhav_copy_zip, get_market_activity_report, get_sec_full_bhav_copy,
    get_fno_participant_wise_volume_data, get_fno_participant_wise_oi_data,
    get_volatility_report)

# modify date to the latest date while testing it out
REPORT_DATE = "02-05-2024"


def test_get_market_activity_report():
    """
    Test get market activity report for a given date
    """
    data = get_market_activity_report(date=REPORT_DATE)
    assert isinstance(data, pd.DataFrame)


def test_get_bhav_copy_zip():
    """
    Test get bhav copy report for a given date
    """
    data = get_bhav_copy_zip(date=REPORT_DATE)
    assert isinstance(data, pd.DataFrame)


def test_get_sec_full_bhav_copy():
    """
    Test get bhav copy report for a given date
    """
    data = get_sec_full_bhav_copy(date=REPORT_DATE)
    assert isinstance(data, pd.DataFrame)


def test_get_fno_participant_wise_volume_data():
    """
    Test get fno daily volume data participant wise
    """
    data = get_fno_participant_wise_volume_data(date=REPORT_DATE)
    assert isinstance(data, pd.DataFrame)


def test_get_fno_participant_wise_oi_data():
    """
    Test get fno daily oi data participant wise
    """
    data = get_fno_participant_wise_oi_data(date=REPORT_DATE)
    assert isinstance(data, pd.DataFrame)


def test_get_volatility_report():
    """
    Test get volatility report download
    """
    data = get_volatility_report(date=REPORT_DATE)
    assert isinstance(data, pd.DataFrame)
