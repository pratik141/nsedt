window_size = 50
max_workers = 10
log_format = """{
    "time": "%(asctime)s",
    "lineno": "%(lineno)d",
    "name": "[%(name)s]",
    "levelname": "%(levelname)s",
    "process": "%(process)s",
    "filename": "%(filename)s",
    "funcName": "%(funcName)s",
    "logmessage": "%(message)s",
}"""

base_url = "https://www.nseindia.com/"
equity_price_histroy = "api/historical/securityArchives?"
equity_corpinfo = "api/corporates-corporateActions?"
marketStatus = "api/marketStatus"
equity_event = "api/event-calendar?"
equity_chart = "api/chart-databyindex?"
equity_info = "api/quote-equity?"
