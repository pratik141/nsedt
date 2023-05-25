import pandas as pd


def price(result):
    columns_required = [
        "CH_TIMESTAMP",
        "CH_OPENING_PRICE",
        "CH_TRADE_HIGH_PRICE",
        "CH_TRADE_LOW_PRICE",
        "CH_CLOSING_PRICE",
        "CH_PREVIOUS_CLS_PRICE",
        "CH_TOT_TRADED_QTY",
        "CH_TOT_TRADED_VAL",
        "CH_52WEEK_HIGH_PRICE",
        "CH_52WEEK_LOW_PRICE",
        "VWAP",
        "COP_DELIV_QTY",
        "COP_DELIV_PERC",
    ]
    try:
        result = result[columns_required]
    except:
        return result
    result = result.set_axis(
        [
            "Date",
            "Open Price",
            "High Price",
            "Low Price",
            "Close Price",
            "Prev Close Price",
            "Total Traded Quantity",
            "Total Traded Value",
            "52 Week High Price",
            "52 Week Low Price",
            "VWAP",
            "Deliverable Volume",
            "Deliverable Percent",
        ],
        axis=1,
    )

    result["Date"] = pd.to_datetime(result["Date"])
    result = result.sort_values("Date", ascending=True)
    result.reset_index(drop=True, inplace=True)
    return result
