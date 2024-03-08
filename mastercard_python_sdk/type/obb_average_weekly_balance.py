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


class RequiredObbAverageWeeklyBalance(TypedDict):
    # Average daily ending balance during the week
    amount: typing.Union[int, float]

    # Begin date of the week
    fromDate: str

    # End date of the week
    toDate: str

    # Week number, where the first week of each year begins on January 1st and ends on January 7th. May be in the range [1, 53]
    week: int

class OptionalObbAverageWeeklyBalance(TypedDict, total=False):
    pass

class ObbAverageWeeklyBalance(RequiredObbAverageWeeklyBalance, OptionalObbAverageWeeklyBalance):
    pass
