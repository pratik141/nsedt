"""
Constants
"""
from .index_symbol import symbol_map

WINDOW_SIZE = 50
MAX_WORKERS = 10
SYMBOL_MAP = symbol_map
LOG_FORMAT = """{
    "time": "%(asctime)s",
    "lineno": "%(lineno)d",
    "name": "[%(name)s]",
    "loglevel": "%(levelname)s",
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
EQUITY_LIST = "api/market-data-pre-open?key=ALL"
ASM_LIST = "api/reportASM"

### Index
INDEX_PRICE_HISTORY = "api/historical/indicesHistory?"

### DERIVATIVES
OPTIONS_PRICE_EQUITIES = "api/option-chain-equities?"
OPTIONS_PRICE_INDICES = "api/option-chain-indices?"
INDICES = ["NIFTY", "FINNIFTY", "BANKNIFTY"]
VIX_HISTORY = "api/historical/vixhistory?"
FUTURES_PRICE = "api/historical/foCPV?"
