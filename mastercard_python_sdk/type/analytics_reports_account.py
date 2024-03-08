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

from mastercard_python_sdk.type.account_analytics import AccountAnalytics
from mastercard_python_sdk.type.account_details import AccountDetails
from mastercard_python_sdk.type.report_transaction import ReportTransaction

class RequiredAnalyticsReportsAccount(TypedDict):
    # The ID of the account
    id: int

    # The account name from the institution
    name: str

    # The account number from the institution (obfuscated)
    number: str

    # One of the values from account types
    type: str

    # a list of transaction records
    transactions: typing.List[ReportTransaction]

class OptionalAnalyticsReportsAccount(TypedDict, total=False):
    # The name(s) of the account owner(s), retrieved from the institution.
    ownerName: str

    # The mailing address of the account owner, retrieved from the institution.
    ownerAddress: str

    # The status of the most recent aggregation attempt
    aggregationStatusCode: int

    # The cleared balance of the account as-of `balanceDate`
    currentBalance: typing.Union[int, float]

    # Available balance
    availableBalance: typing.Union[int, float]

    # A timestamp showing when the `balance` was captured
    balanceDate: int

    details: AccountDetails

    accountAnalytics: AccountAnalytics

class AnalyticsReportsAccount(RequiredAnalyticsReportsAccount, OptionalAnalyticsReportsAccount):
    pass
