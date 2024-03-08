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


class RequiredBalanceAndCashFlowAnalyticsReportConstraints(TypedDict):
    pass

class OptionalBalanceAndCashFlowAnalyticsReportConstraints(TypedDict, total=False):
    # The list of account IDs to include in the report. If omitted, all accounts on record for the customer will be used.
    accountIds: typing.List[int]

    # Number of days to search for transactions. Must be one of 30, 90, 180, 270, 365, or 730. If omitted, defaults to 2 years from current time at which the request was received (730 days).
    lengthOfReport: int

class BalanceAndCashFlowAnalyticsReportConstraints(RequiredBalanceAndCashFlowAnalyticsReportConstraints, OptionalBalanceAndCashFlowAnalyticsReportConstraints):
    pass
