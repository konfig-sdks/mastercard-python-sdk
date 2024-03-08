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


class RequiredCashFlowTransactionAnalyticsAttributesLastTransactionDateItem(TypedDict):
    # Date the deposit transaction was posted
    date: str

class OptionalCashFlowTransactionAnalyticsAttributesLastTransactionDateItem(TypedDict, total=False):
    # Amount of transaction if deposit, otherwise null
    depositsCredits: typing.Union[int, float]

    # Amount of transaction if withdrawal, otherwise null
    withdrawalsDebits: typing.Union[int, float]

    # Amount of transaction if zero, otherwise null
    zeroAmountTransaction: typing.Union[int, float]

    # Description of transaction
    transactionDescription: str

class CashFlowTransactionAnalyticsAttributesLastTransactionDateItem(RequiredCashFlowTransactionAnalyticsAttributesLastTransactionDateItem, OptionalCashFlowTransactionAnalyticsAttributesLastTransactionDateItem):
    pass
