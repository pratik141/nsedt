"""
  Test case for nsedt.reports
"""

import pandas as pd
from nsedt.reports import get_bhav_copy_zip, get_market_activity_report

# modify date to the latest date
REPORT_DATE = "02-05-2024"


def test_get_market_activity_report():
    """
    Test get market activity report for a given date
    """
    data = get_market_activity_report(date=REPORT_DATE)
    assert isinstance(data, bytes)


def test_get_bhav_copy_zip():
    """
    Test get bhav copy report for a given date
    """
    data = get_bhav_copy_zip(date=REPORT_DATE)
    assert isinstance(data, pd.DataFrame)
