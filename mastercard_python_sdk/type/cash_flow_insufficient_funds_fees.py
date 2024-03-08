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

from mastercard_python_sdk.type.insufficient_funds_transaction import InsufficientFundsTransaction

class RequiredCashFlowInsufficientFundsFees(TypedDict):
    pass

class OptionalCashFlowInsufficientFundsFees(TypedDict, total=False):
    # Count of all NSF transactions during the report
    countOfTransactionsForTheReportTimePeriod: int

    # Sum of all NSF transactions during the report
    sumOfTransactionsForTheReportTimePeriod: typing.Union[int, float]

    # Transactions categorized as NSF
    transactions: typing.List[InsufficientFundsTransaction]

class CashFlowInsufficientFundsFees(RequiredCashFlowInsufficientFundsFees, OptionalCashFlowInsufficientFundsFees):
    pass
