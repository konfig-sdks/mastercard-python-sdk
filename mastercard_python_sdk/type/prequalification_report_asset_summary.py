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


class RequiredPrequalificationReportAssetSummary(TypedDict):
    # The current balance of the account
    currentBalance: typing.Union[int, float]

    # The two month average daily balance of the account
    twoMonthAverage: typing.Union[int, float]

    # The beginning balance of the account per the time period of the report
    beginningBalance: typing.Union[int, float]

class OptionalPrequalificationReportAssetSummary(TypedDict, total=False):
    # The asset type: \"checking\", \"savings\", \"moneyMarket\", \"cd\", \"investment\"
    type: str

    # The available balance for the account
    availableBalance: typing.Union[int, float]

    # The six month average daily balance of the account
    sixMonthAverage: typing.Union[int, float]

class PrequalificationReportAssetSummary(RequiredPrequalificationReportAssetSummary, OptionalPrequalificationReportAssetSummary):
    pass
