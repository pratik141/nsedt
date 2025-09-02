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
        "CH_LAST_TRADED_PRICE",
        "CH_TOT_TRADED_QTY",
        "CH_TOT_TRADED_VAL",
        # "CH_52WEEK_HIGH_PRICE",
        # "CH_52WEEK_LOW_PRICE",
        "VWAP",
        "COP_DELIV_QTY",
        "COP_DELIV_PERC",
        "CH_SERIES",
    ]

    try:
        result = result[columns_required]
    except Exception as e:  # pylint: disable=W0702
        print(f"No data found for the given input: {e}")
        return result
    result = result.set_axis(
        [
            "Date",
            "Open Price",
            "High Price",
            "Low Price",
            "Close Price",
            "Prev Close Price",
            "Last Traded Price",
            "Total Traded Quantity",
            "Total Traded Value",
            # "52 Week High Price",  # Not available in api
            # "52 Week Low Price",  # Not available in api
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


def indices(
    data_json,
    columns_drop_list: list = None,
    columns_rename_map: map = None,
):
    """
    Args:
        data_json (json):  data in json format
    Returns:
        Pandas DataFrame: df with indexCloseOnlineRecords and indexTurnoverRecords
    """
    if columns_drop_list:
        columns_list = columns_drop_list
    else:
        columns_list = ["_id", "EOD_INDEX_NAME", "TIMESTAMP"]

    if columns_rename_map:
        columns_rename = columns_rename_map
    else:
        columns_rename = {
            "EOD_OPEN_INDEX_VAL": "Open Price",
            "EOD_HIGH_INDEX_VAL": "High Price",
            "EOD_CLOSE_INDEX_VAL": "Close Price",
            "EOD_LOW_INDEX_VAL": "Low Price",
            "EOD_TIMESTAMP": "Date",
        }
    data_close_df = (
        pd.DataFrame(data_json["data"]["indexCloseOnlineRecords"])
        .drop(columns=columns_list)
        .rename(columns=columns_rename)
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
    """_summary_

    Args:
        data_json (str): _description_
        response_type (str): _description_

    Returns:
        _type_: _description_
    """
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
    data_json: object,
    response_type: str = "panda_df",
    columns_drop_list: list = None,
):
    """
        Format Vix data
    Args:
        data_json (object): data in json format.
        response_type (str, optional): response_type. Defaults to "panda_df".
        columns_drop_list (list, optional): custom columns drop list. Defaults to None.
    Returns:
        _type_: _description_
    """
    data_json = data_json["data"]
    if columns_drop_list:
        columns_list = columns_drop_list
    else:
        columns_list = [
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
    if response_type == "json":
        data_json_ret = []
        for record in data_json:
            for column in columns_list:
                record.pop(column, None)

            data_json_ret.append(record)
        return data_json_ret

    return (
        pd.json_normalize(data_json)
        .drop(columns=columns_list)
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


def derivatives_futures(
    data_json: str,
    response_type: str = "panda_df",
    columns_drop_list=None,
):
    """
        Format futures data

    Args:
        data_json (object): data in json format.
        response_type (str, optional): response_type. Defaults to "panda_df".
        columns_drop_list (list, optional): custom columns drop list. Defaults to None.

    Returns:
            json: format data in json
        or
            dataframe: format data in panda df
    """
    if columns_drop_list:
        columns_list = columns_drop_list
    else:
        columns_list = [
            "_id",
            "FH_MARKET_LOT",
            "FH_MARKET_TYPE",
            "FH_OPTION_TYPE",
            "FH_SYMBOL",
            "FH_INSTRUMENT",
            "FH_STRIKE_PRICE",
            "FH_LAST_TRADED_PRICE",
            "TIMESTAMP",
        ]
    if response_type == "json":
        data_json_ret = []
        for record in data_json:
            for column in columns_list:
                record.pop(column, None)
            data_json_ret.append(record)
        return data_json_ret

    return (
        pd.json_normalize(data_json)
        .drop(columns=columns_list)
        .rename(
            columns={
                "FH_OPENING_PRICE": "Open Price",
                "FH_TRADE_HIGH_PRICE": "High Price",
                "FH_CLOSING_PRICE": "Close Price",
                "FH_TRADE_LOW_PRICE": "Low Price",
                "FH_CHANGE_IN_OI": "Change in OI",
                "FH_EXPIRY_DT": "Expiry Date",
                "FH_TIMESTAMP": "Date",
            }
        )
    )


def derivaties_options(
    data_json: str,
    response_type: str = "panda_df",
    columns_drop_list=None,
):
    """
        Format historical options data

    Args:
        data_json (object): data in json format.
        response_type (str, optional): response_type. Defaults to "panda_df".
        columns_drop_list (list, optional): custom columns drop list. Defaults to None.

    Returns:
            json: format data in json
        or
            dataframe: format data in panda df
    """
    if data_json:
        data_json = data_json['data']
    if columns_drop_list:
        columns_list = columns_drop_list
    else:
        columns_list = [
            "_id",
            "FH_MARKET_LOT",
            "FH_MARKET_TYPE",
            "FH_OPTION_TYPE",
            "FH_SYMBOL",
            "FH_INSTRUMENT",
            "FH_STRIKE_PRICE",
            "FH_LAST_TRADED_PRICE",
            "TIMESTAMP",
        ]

    if response_type == "json":
        data_json_ret = []
        for record in data_json:
            for column in columns_list:
                record.pop(column, None)
            data_json_ret.append(record)
        return data_json_ret

    return (
        pd.json_normalize(data_json)
        .drop(columns=columns_list)
        .rename(
            columns={
                "FH_OPENING_PRICE": "Open Price",
                "FH_TRADE_HIGH_PRICE": "High Price",
                "FH_CLOSING_PRICE": "Close Price",
                "FH_TRADE_LOW_PRICE": "Low Price",
                "FH_CHANGE_IN_OI": "Change in OI",
                "FH_EXPIRY_DT": "Expiry Date",
                "FH_TIMESTAMP": "Date",
            }
        )
    )
