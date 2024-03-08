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


class RequiredObbDateRangeAndAmount(TypedDict):
    # Period represented by this metric
    period: str

    # Begin date of the period being reported
    periodBeginDate: str

    # End date of the period being reported
    periodEndDate: str

class OptionalObbDateRangeAndAmount(TypedDict, total=False):
    # Metric value for the given period
    amount: typing.Union[int, float]

class ObbDateRangeAndAmount(RequiredObbDateRangeAndAmount, OptionalObbDateRangeAndAmount):
    pass
