"""
return data in specific format
"""

import pandas as pd


def price(result):
    """
    Args:
        result (Pandas DataFrame): result
    Returns:
        Pandas DataFrame: df containing data in specific format
    """

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
        "CH_SERIES",
    ]
    try:
        result = result[columns_required]
    except:  # pylint: disable=W0702
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
            "Series",
        ],
        axis=1,
    )

    result["Date"] = pd.to_datetime(result["Date"])
    result = result.sort_values("Date", ascending=True)
    result.reset_index(drop=True, inplace=True)
    return result


def indices(data_json):
    """
    Args:
        data_json (json):  data in json format
    Returns:
        Pandas DataFrame: df with indexCloseOnlineRecords and indexTurnoverRecords
    """
    data_close_df = (
        pd.DataFrame(data_json["data"]["indexCloseOnlineRecords"])
        .drop(columns=["_id", "EOD_INDEX_NAME", "TIMESTAMP"])
        .rename(
            columns={
                "EOD_OPEN_INDEX_VAL": "Open Price",
                "EOD_HIGH_INDEX_VAL": "High Price",
                "EOD_CLOSE_INDEX_VAL": "Close Price",
                "EOD_LOW_INDEX_VAL": "Low Price",
                "EOD_TIMESTAMP": "Date",
            }
        )
    )

    ## Mismatch values
    # data_turnover_df = (
    #     pd.DataFrame(d["data"]["indexTurnoverRecords"])
    #     .drop(columns=["_id", "HIT_INDEX_NAME_UPPER", "HIT_TIMESTAMP"])
    #     .rename(
    #         columns={
    #             "HIT_TRADED_QTY": "Total Traded Quantity",
    #             "HIT_TURN_OVER": "Total Traded Value",
    #             "TIMESTAMP": "Date",
    #         }
    #     )
    # )
    return data_close_df
    # return pd.merge(data_close_df, data_turnover_df, on="Date", how="inner")


def option_chain(
    data_json: str,
    response_type: str,
):
    if response_type == "json":
        data_json_ret = []
        for record in data_json:
            if "PE" in record:
                record["PE"].pop("strikePrice", None)
                record["PE"].pop("expiryDate", None)
                record["PE"].pop("underlying", None)
                record["PE"].pop("identifier", None)
            if "CE" in record:
                record["CE"].pop("strikePrice", None)
                record["CE"].pop("expiryDate", None)
                record["CE"].pop("underlying", None)
                record["CE"].pop("identifier", None)
            data_json_ret.append(record)
        return data_json_ret

    return (
        pd.json_normalize(data_json)
        .sort_values(by=["expiryDate", "strikePrice"], ascending=True)
        .drop(
            columns=[
                "PE.strikePrice",
                "PE.expiryDate",
                "PE.identifier",
                "CE.strikePrice",
                "CE.expiryDate",
                "CE.identifier",
            ]
        )
    )


def get_vix(
    data_json: str,
    response_type: str = "panda_df",
):
    data_json = data_json["data"]
    if response_type == "json":
        data_json_ret = []
        for record in data_json:
            if "PE" in record:
                record.pop("_id", None)
                record.pop("TIMESTAMP", None)
                record.pop("createdAt", None)
                record.pop("updatedAt", None)
                record.pop("__v", None)
                record.pop("ALTERNATE_INDEX_NAME", None)
                record.pop("EOD_INDEX_NAME", None)
                record.pop("EOD_PREV_CLOSE", None)
                record.pop("VIX_PTS_CHG", None)
                record.pop("VIX_PERC_CHG", None)
            data_json_ret.append(record)
        return data_json_ret

    return (
        pd.json_normalize(data_json)
        .drop(
            columns=[
                "_id",
                "TIMESTAMP",
                "createdAt",
                "updatedAt",
                "__v",
                "ALTERNATE_INDEX_NAME",
                "EOD_INDEX_NAME",
                "EOD_PREV_CLOSE",
                "VIX_PTS_CHG",
                "VIX_PERC_CHG",
            ]
        )
        .rename(
            columns={
                "EOD_OPEN_INDEX_VAL": "Open Price",
                "EOD_HIGH_INDEX_VAL": "High Price",
                "EOD_CLOSE_INDEX_VAL": "Close Price",
                "EOD_LOW_INDEX_VAL": "Low Price",
                "EOD_TIMESTAMP": "Date",
            }
        )
    )
