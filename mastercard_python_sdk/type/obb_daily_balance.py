# coding: utf-8

"""
    Open Banking

    OpenAPI specification for Finicity APIs.  Open Banking solutions in the US are provided by Finicity, a Mastercard company.

    The version of the OpenAPI document: 1.16.0
    Contact: apisupport@mastercard.com
    Created by: https://developer.mastercard.com/open-banking-us/documentation/support/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredObbDailyBalance(TypedDict):
    # Date of balance information
    date: str

    # Day of the week for which balance information available
    dayOfWeek: str

    # End of day balance
    endingBalance: typing.Union[int, float]

class OptionalObbDailyBalance(TypedDict, total=False):
    pass

class ObbDailyBalance(RequiredObbDailyBalance, OptionalObbDailyBalance):
    pass
