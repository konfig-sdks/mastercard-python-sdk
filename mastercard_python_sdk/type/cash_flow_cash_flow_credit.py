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

from mastercard_python_sdk.type.cash_flow_monthly_cash_flow_credits import CashFlowMonthlyCashFlowCredits

class RequiredCashFlowCashFlowCredit(TypedDict):
    # List of attributes for each month
    monthlyCashFlowCredits: typing.List[CashFlowMonthlyCashFlowCredits]

class OptionalCashFlowCashFlowCredit(TypedDict, total=False):
    # Sum of all credit transactions for each month by account
    twelveMonthCreditTotal: typing.Union[int, float]

    # Sum of all monthly credit transactions without transfers for the account
    twelveMonthCreditTotalLessTransfers: typing.Union[int, float]

    # Sum of six month credit transactions
    sixMonthCreditTotal: typing.Union[int, float]

    # Sum of six month credit transactions without transfers
    sixMonthCreditTotalLessTransfers: typing.Union[int, float]

    # Sum of two month credit transactions
    twoMonthCreditTotal: typing.Union[int, float]

    # Sum of two month credit transactions without transfers
    twoMonthCreditTotalLessTransfers: typing.Union[int, float]

class CashFlowCashFlowCredit(RequiredCashFlowCashFlowCredit, OptionalCashFlowCashFlowCredit):
    pass
