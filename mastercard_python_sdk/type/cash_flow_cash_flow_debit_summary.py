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

from mastercard_python_sdk.type.cash_flow_monthly_cash_flow_debit_summaries import CashFlowMonthlyCashFlowDebitSummaries

class RequiredCashFlowCashFlowDebitSummary(TypedDict):
    # List of attributes for each month
    monthlyCashFlowDebitSummaries: typing.List[CashFlowMonthlyCashFlowDebitSummaries]

    # Sum of all monthly debit transactions for each month by account
    twelveMonthDebitTotal: typing.Union[int, float]

    # Sum of all monthly debit transactions without transfers for the account
    twelveMonthDebitTotalLessTransfers: typing.Union[int, float]

    # Six month sum of all debit transactions by account
    sixMonthDebitTotal: typing.Union[int, float]

    # Six month sum of all debit transactions without transfers for the account
    sixMonthDebitTotalLessTransfers: typing.Union[int, float]

    # Two month sum of all debit transactions by account
    twoMonthDebitTotal: typing.Union[int, float]

    # Two month sum of all debit transactions without transfers for the account
    twoMonthDebitTotalLessTransfers: typing.Union[int, float]

class OptionalCashFlowCashFlowDebitSummary(TypedDict, total=False):
    pass

class CashFlowCashFlowDebitSummary(RequiredCashFlowCashFlowDebitSummary, OptionalCashFlowCashFlowDebitSummary):
    pass
