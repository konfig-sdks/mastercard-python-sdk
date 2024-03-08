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


class RequiredCashFlowMonthlycashflowDebits(TypedDict):
    # One instance for each complete calendar month in the report
    month: int

    # Number of Debits by month
    numberOfDebits: str

    # Total Amount of Debits by month
    totalDebitsAmount: typing.Union[int, float]

    # Largest Debit by month
    largestDebit: typing.Union[int, float]

    # Number of Debits by month (less transfers)
    numberOfDebitsLessTransfers: str

    # Total amount of debits by month (less transfers)
    totalDebitsAmountLessTransfers: typing.Union[int, float]

    # The average debit amount
    averageDebitAmount: typing.Union[int, float]

class OptionalCashFlowMonthlycashflowDebits(TypedDict, total=False):
    pass

class CashFlowMonthlycashflowDebits(RequiredCashFlowMonthlycashflowDebits, OptionalCashFlowMonthlycashflowDebits):
    pass
