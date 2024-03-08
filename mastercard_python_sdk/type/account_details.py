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


class RequiredAccountDetails(TypedDict):
    pass

class OptionalAccountDetails(TypedDict, total=False):
    # Only available for investment accounts. Net interest earned after deducting interest paid out.
    interestMarginBalance: typing.Union[int, float]

    # Only available for investment accounts. Amount available for cash withdrawal.
    availableCashBalance: typing.Union[int, float]

    # Only available for investment accounts. Vested amount in account.
    vestedBalance: typing.Union[int, float]

    # Only available for investment accounts. Current loan balance.
    currentLoanBalance: typing.Union[int, float]

    # The available balance for the account
    availableBalanceAmount: typing.Union[int, float]

class AccountDetails(RequiredAccountDetails, OptionalAccountDetails):
    pass
