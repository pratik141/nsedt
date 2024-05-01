"""_summary_

Returns:
    _type_: _description_
"""


class MissingEnvValue(BaseException):
    """_summary_

    Args:
        BaseException (_type_): _description_
    """

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f""" ----[ERROR]----
=================================================================================================
{self.message}
=================================================================================================
"""


class DateStrikePriceOutofRange(BaseException):
    """_summary_

    Args:
        BaseException (_type_): _description_
    """

    def __str__(self):
        return """ ----[ERROR]----
=================================================================================================
Either Date of strike Price is out of range for NSE (No data found)
=================================================================================================
"""
