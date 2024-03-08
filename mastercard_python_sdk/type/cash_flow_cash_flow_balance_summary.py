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

from mastercard_python_sdk.type.cash_flow_monthly_cash_flow_balance_summaries import CashFlowMonthlyCashFlowBalanceSummaries

class RequiredCashFlowCashFlowBalanceSummary(TypedDict):
    # List of attributes for each month
    monthlyCashFlowBalanceSummaries: typing.List[CashFlowMonthlyCashFlowBalanceSummaries]

    # Min Daily Balance across entire transaction history  for all accounts
    minDailyBalance: typing.Union[int, float]

    # Max Daily Balance across entire transaction history for all accounts
    maxDailyBalance: typing.Union[int, float]

    # Average Daily Balance across twelve months for all accounts
    twelveMonthAverageDailyBalance: typing.Union[int, float]

    # Average Daily Balance across six months for all accounts
    sixMonthAverageDailyBalance: typing.Union[int, float]

    # Average Daily Balance across two months for all accounts
    twoMonthAverageDailyBalance: typing.Union[int, float]

    # Standard Deviation of Daily Balance across twelve months for all accounts
    twelveMonthStandardDeviationOfDailyBalance: str

    # Standard Deviation of Daily Balance across two months for all accounts
    twoMonthStandardDeviationOfDailyBalance: str

    # Number of Days Negative Balance over entire transaction history for all accounts
    numberOfDaysNegativeBalance: str

    # Number of Days Positive Balance over entire transaction history for all accounts
    numberOfDaysPositiveBalance: str

class OptionalCashFlowCashFlowBalanceSummary(TypedDict, total=False):
    # Standard Deviation of Daily Balance across six months for all accounts
    sixMonthStandardDeviationOfDailyBalance: str

class CashFlowCashFlowBalanceSummary(RequiredCashFlowCashFlowBalanceSummary, OptionalCashFlowCashFlowBalanceSummary):
    pass
