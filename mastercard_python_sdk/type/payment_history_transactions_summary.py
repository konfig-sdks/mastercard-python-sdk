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


class RequiredPaymentHistoryTransactionsSummary(TypedDict):
    # Total of NSF transactions
    totalNonSufficientFunds: typing.Union[int, float]

    # Monthly average of NSF transactions
    averageMonthlyNonSufficientFunds: typing.Union[int, float]

    # Total of deposit transactions
    totalDeposits: typing.Union[int, float]

    # Monthly average of deposit transactions
    averageMonthlyDeposits: typing.Union[int, float]

    # Total of withdrawals transactions
    totalWithdrawals: typing.Union[int, float]

    # Monthly average of withdrawal transactions
    averageMonthlyWithdrawals: typing.Union[int, float]

    # ISO-8601 date of earliest transaction
    beginDate: str

    # ISO-8601 date of latest transaction
    endDate: str

class OptionalPaymentHistoryTransactionsSummary(TypedDict, total=False):
    pass

class PaymentHistoryTransactionsSummary(RequiredPaymentHistoryTransactionsSummary, OptionalPaymentHistoryTransactionsSummary):
    pass
