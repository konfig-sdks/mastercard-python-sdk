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


class RequiredReportTransactionBase2(TypedDict):
    pass

class OptionalReportTransactionBase2(TypedDict, total=False):
    # A normalized payee, derived from the transaction's `description` and `memo` fields
    normalizedPayee: str

    # The unique identifier given by the FI for each transaction
    institutionTransactionId: str

    # One of the values from Categories (assigned based on the payee name)
    category: str

    # One of the values from transaction types
    type: str

    # The type of investment security (VOA only)
    securityType: str

    # Investment symbol (VOA only)
    symbol: str

    # A commission amount
    commission: typing.Union[int, float]

class ReportTransactionBase2(RequiredReportTransactionBase2, OptionalReportTransactionBase2):
    pass
