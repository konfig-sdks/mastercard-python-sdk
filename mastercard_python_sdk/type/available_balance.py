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


class RequiredAvailableBalance(TypedDict):
    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    id: int

    # The last 4 digits of the ACH account number
    realAccountNumberLast4: str

    # The available balance of the account
    availableBalance: typing.Union[int, float]

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    availableBalanceDate: int

    # The cleared balance of the account. Also referred as posted balance, current balance, ledger balance
    clearedBalance: typing.Union[int, float]

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    clearedBalanceDate: int

    # The status of the most recent aggregation attempt (see [Aggregation Status Codes](https://developer.mastercard.com/open-banking-us/documentation/products/manage/account-aggregation/#aggregation-status-codes)). Won't be present until you have run your first aggregation for the account.
    aggregationStatusCode: int

    # A currency code
    currency: str

class OptionalAvailableBalance(TypedDict, total=False):
    pass

class AvailableBalance(RequiredAvailableBalance, OptionalAvailableBalance):
    pass
