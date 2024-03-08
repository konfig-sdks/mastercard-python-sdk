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

from mastercard_python_sdk.type.cash_flow_monthly_cash_flow_credit_summaries import CashFlowMonthlyCashFlowCreditSummaries

class RequiredCashFlowCashFlowCreditSummary(TypedDict):
    # List of attributes for each month
    monthlyCashFlowCreditSummaries: typing.List[CashFlowMonthlyCashFlowCreditSummaries]

    # Sum of all credit transactions for each month for all accounts
    twelveMonthCreditTotal: typing.Union[int, float]

    # Sum of all monthly credit transactions without transfers for all accounts
    twelveMonthCreditTotalLessTransfers: typing.Union[int, float]

    # Six month sum of all credit transactions
    sixMonthCreditTotal: typing.Union[int, float]

    # Six month sum of all monthly credit transactions without transfers for all accounts
    sixMonthCreditTotalLessTransfers: typing.Union[int, float]

    # Two month sum of all credit transactions
    twoMonthCreditTotal: typing.Union[int, float]

    # Two month sum of all monthly credit transactions without transfers for all accounts
    twoMonthCreditTotalLessTransfers: typing.Union[int, float]

class OptionalCashFlowCashFlowCreditSummary(TypedDict, total=False):
    pass

class CashFlowCashFlowCreditSummary(RequiredCashFlowCashFlowCreditSummary, OptionalCashFlowCashFlowCreditSummary):
    pass
