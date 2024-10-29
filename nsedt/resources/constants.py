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
REPORT_URL = "https://nsearchives.nseindia.com/"

### EQUITY
EQUITY_PRICE_HISTORY = "api/historical/securityArchives?"
EQUITY_CORPINFO = "api/corporates-corporateActions?"
MARKETSTATUS = "api/marketStatus"
EQUITY_EVENT = "api/event-calendar?"
EQUITY_CHART = "api/chart-databyindex?"
EQUITY_INFO = "api/quote-equity?"
EQUITY_LIST = "api/market-data-pre-open?key=ALL"
ASM_LIST = "api/reportASM"

BULK_DEAL = "api/historical/bulk-deals?"
BLOCK_DEAL = "api/historical/block-deals?"
SHORT_SELLING = "api/historical/short-selling?"

TOP_ACTIVE = "api/live-analysis-most-active-securities?"
TOP_GAINERS = "/api/liveanalysis/gainers/allSec"
TOP_GAINERS = "/api/liveanalysis/loosers/allSec"

### Index
INDEX_PRICE_HISTORY = "api/historical/indicesHistory?"

### DERIVATIVES
OPTIONS_PRICE_EQUITIES = "api/option-chain-equities?"
OPTIONS_PRICE_INDICES = "api/option-chain-indices?"
INDICES = ["NIFTY", "FINNIFTY", "BANKNIFTY"]
VIX_HISTORY = "api/historical/vixhistory?"
FNO_HISTORY = "api/historical/foCPV?"

# Reports
MARKET_ACTIVITY_REPORT = "archives/equities/mkt/MA"
BHAV_COPY_REPORT = "content/historical/EQUITIES/2024/"
SEC_BHAV_COPY_REPORT =  "products/content/"
NSCCL_REPORTS = "content/nsccl/"
NSCCL_VOLT = "archives/nsccl/volt/"
