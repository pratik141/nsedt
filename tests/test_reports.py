"""
  Test case for nsedt.reports
"""

from nsedt.reports import get_bhav_copy_zip, get_market_activity_report

# modify date to the latest date
MA_ACTIVITY_DATE = "020524"
BHAV_COPY_DATE = "02MAR2024"
BHAV_COPY_FILE_PATH = "/home/"



def test_get_market_activity_report():
    """
    Test get market activity report for a given date
    """
    data = get_market_activity_report(date=MA_ACTIVITY_DATE)
    assert isinstance(data, bytes)


def test_get_bhav_copy_zip():
    """
    Test get bhav copy report for a given date
    """
    data = get_bhav_copy_zip(date=BHAV_COPY_DATE, file_path="")
    assert isinstance(data, bool)
