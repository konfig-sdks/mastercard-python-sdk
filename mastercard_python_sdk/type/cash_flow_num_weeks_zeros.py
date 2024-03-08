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

from mastercard_python_sdk.type.obb_week_of_year import ObbWeekOfYear

class RequiredCashFlowNumWeeksZeros(TypedDict):
    # Number of weeks during known history of account in which data was available
    historicNumberOfWeeksWithDataAvailable: int

    # Number of weeks during known history of account where zero transactions were posted
    historicNumberOfWeeksZeroTransactions: int

    # List of weeks with zero reported transactions
    historicWeeksWithZeroTransactions: typing.List[ObbWeekOfYear]

class OptionalCashFlowNumWeeksZeros(TypedDict, total=False):
    pass

class CashFlowNumWeeksZeros(RequiredCashFlowNumWeeksZeros, OptionalCashFlowNumWeeksZeros):
    pass
