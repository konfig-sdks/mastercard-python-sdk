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


class RequiredObbDateRangeAndCount(TypedDict):
    # Count of occurrences for the given period
    count: int

    # Period represented by this metric
    period: str

    # Begin date of the period being reported
    periodBeginDate: str

    # End date of the period being reported
    periodEndDate: str

class OptionalObbDateRangeAndCount(TypedDict, total=False):
    pass

class ObbDateRangeAndCount(RequiredObbDateRangeAndCount, OptionalObbDateRangeAndCount):
    pass
