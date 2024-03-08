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


class RequiredCashFlowMonthlyCashFlowBalanceSummaries(TypedDict):
    # One instance for each complete calendar month in the report
    month: int

    # Min Daily Balance for each month for all accounts
    minDailyBalance: typing.Union[int, float]

    # Max Daily Balance for each month for all accounts
    maxDailyBalance: typing.Union[int, float]

    # Average Daily Balance for each month for all accounts
    averageDailyBalance: typing.Union[int, float]

    # Number of Days Negative Balance for each month for all accounts
    numberOfDaysNegativeBalance: str

    # Number of Days Positive Balance for each month for all accounts
    numberOfDaysPositiveBalance: str

class OptionalCashFlowMonthlyCashFlowBalanceSummaries(TypedDict, total=False):
    # Standard Deviation of Daily Balance for each month for all accounts
    standardDeviationOfDailyBalance: str

class CashFlowMonthlyCashFlowBalanceSummaries(RequiredCashFlowMonthlyCashFlowBalanceSummaries, OptionalCashFlowMonthlyCashFlowBalanceSummaries):
    pass
