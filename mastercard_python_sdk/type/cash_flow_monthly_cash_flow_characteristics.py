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


class RequiredCashFlowMonthlyCashFlowCharacteristics(TypedDict):
    # One instance for each complete calendar month in the report
    month: int

    # Total Credits - Total Debits by month
    totalCreditsLessTotalDebits: typing.Union[int, float]

    # Total Credits - Total Debits by month (Without Transfers)
    totalCreditsLessTotalDebitsLessTransfers: typing.Union[int, float]

    # Average transaction amount by month
    averageTransactionAmount: typing.Union[int, float]

class OptionalCashFlowMonthlyCashFlowCharacteristics(TypedDict, total=False):
    pass

class CashFlowMonthlyCashFlowCharacteristics(RequiredCashFlowMonthlyCashFlowCharacteristics, OptionalCashFlowMonthlyCashFlowCharacteristics):
    pass
