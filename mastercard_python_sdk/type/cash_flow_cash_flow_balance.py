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

from mastercard_python_sdk.type.cash_flow_monthly_cash_flow_balances import CashFlowMonthlyCashFlowBalances

class RequiredCashFlowCashFlowBalance(TypedDict):
    # List of attributes for each month
    monthlyCashFlowBalances: typing.List[CashFlowMonthlyCashFlowBalances]

    # Min daily balance across entire transaction history
    minDailyBalance: typing.Union[int, float]

    # Max Daily Balance across entire transaction history
    maxDailyBalance: typing.Union[int, float]

    # Average Daily Balance across twelve months for the account
    twelveMonthAverageDailyBalance: typing.Union[int, float]

    # Average Daily Balance across six months for the account
    sixMonthAverageDailyBalance: typing.Union[int, float]

    # Average Daily Balance across two months for the account
    twoMonthAverageDailyBalance: typing.Union[int, float]

    # Standard Deviation of Daily Balance across twelve months for the account
    twelveMonthStandardDeviationOfDailyBalance: str

    # Standard Deviation of Daily Balance across two months for the account
    twoMonthStandardDeviationOfDailyBalance: str

    # Number of Days positive balance over entire transaction history
    numberOfDaysPositiveBalance: str

class OptionalCashFlowCashFlowBalance(TypedDict, total=False):
    # Standard Deviation of Daily Balance across six months for the account
    sixMonthStandardDeviationOfDailyBalance: str

    # Number of Days Negative Balance over entire transaction history
    numberDaysNegativeBalance: str

class CashFlowCashFlowBalance(RequiredCashFlowCashFlowBalance, OptionalCashFlowCashFlowBalance):
    pass
