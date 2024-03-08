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

from mastercard_python_sdk.type.cash_flow_monthlycashflow_debits import CashFlowMonthlycashflowDebits

class RequiredCashFlowCashFlowDebit(TypedDict):
    # List of attributes for each month
    monthlyCashFlowDebits: typing.List[CashFlowMonthlycashflowDebits]

class OptionalCashFlowCashFlowDebit(TypedDict, total=False):
    # Sum of all monthly debit transactions for each month by account
    twelveMonthDebitTotal: typing.Union[int, float]

    # Sum of all monthly debit transactions without transfers for the account
    twelveMonthDebitTotalLessTransfers: typing.Union[int, float]

    # Six month sum of all debit transactions
    sixMonthDebitTotal: typing.Union[int, float]

    # Six month sum of all debit transactions without transfers for the account
    sixMonthDebitTotalLessTransfers: typing.Union[int, float]

    # Two month sum of all debit transactions
    twoMonthDebitTotal: typing.Union[int, float]

    # Two month sum of all debit transactions without transfers for the account
    twoMonthDebitTotalLessTransfers: typing.Union[int, float]

class CashFlowCashFlowDebit(RequiredCashFlowCashFlowDebit, OptionalCashFlowCashFlowDebit):
    pass
