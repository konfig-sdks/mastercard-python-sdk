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


class RequiredAnnualIncome(TypedDict):
    # The year for the amounts given in YTD totals for an employer
    year: str

    # Year to date (YTD) gross pay amount for the indicated year
    grossPayAmountYTD: typing.Union[int, float]

class OptionalAnnualIncome(TypedDict, total=False):
    # Year to date (YTD) net pay amount for the indicated year
    netPayAmountYTD: typing.Union[int, float]

    # Year to date (YTD) base pay amount for the year indicated
    basePayAmountYTD: typing.Union[int, float]

    # Year to date (YTD) overtime pay amount for the year indicated
    overtimePayAmountYTD: typing.Union[int, float]

    # Year to date (YTD) other pay amount for the indicated year. Other pay is pay that is not categorized into one of the other categories.
    otherPayAmountYTD: typing.Union[int, float]

    # Year to date (YTD) commission pay amount for the indicated year
    commissionPayAmount: typing.Union[int, float]

class AnnualIncome(RequiredAnnualIncome, OptionalAnnualIncome):
    pass
