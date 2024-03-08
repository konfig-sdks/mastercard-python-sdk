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


class RequiredDirectDeposit(TypedDict):
    pass

class OptionalDirectDeposit(TypedDict, total=False):
    # The amount of the deposit
    amountCurrent: typing.Union[int, float]

    # The last four numbers of the account the deposit went into
    accountLastFour: str

class DirectDeposit(RequiredDirectDeposit, OptionalDirectDeposit):
    pass
