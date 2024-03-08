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


class RequiredNetMonthly(TypedDict):
    # Timestamp for the first day of this month
    month: int

    # Total income during the given month, across all income streams
    net: typing.Union[int, float]

class OptionalNetMonthly(TypedDict, total=False):
    pass

class NetMonthly(RequiredNetMonthly, OptionalNetMonthly):
    pass
