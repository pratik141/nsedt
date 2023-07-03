"""
Constants
"""

WINDOW_SIZE = 50
MAX_WORKERS = 10
LOG_FORMAT = """{
    "time": "%(asctime)s",
    "lineno": "%(lineno)d",
    "name": "[%(name)s]",
    "levelname": "%(levelname)s",
    "process": "%(process)s",
    "filename": "%(filename)s",
    "funcName": "%(funcName)s",
    "logmessage": "%(message)s",
}"""

BASE_URL = "https://www.nseindia.com/"

### EQUITY
EQUITY_PRICE_HISTORY = "api/historical/securityArchives?"
EQUITY_CORPINFO = "api/corporates-corporateActions?"
MARKETSTATUS = "api/marketStatus"
EQUITY_EVENT = "api/event-calendar?"
EQUITY_CHART = "api/chart-databyindex?"
EQUITY_INFO = "api/quote-equity?"

### Index
INDEX_PRICE_HISTORY = "api/historical/indicesHistory?"

### DERIVATIVES
DERIVATIVES_PRICE = "api/option-chain-equities?"
