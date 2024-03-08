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


class RequiredInsufficientFundsTransaction(TypedDict):
    # Amount of the NSF transaction
    amount: typing.Union[int, float]

    # Posted date of the NSF transaction
    postedDate: str

    # Finicity transaction ID
    transactionId: int

class OptionalInsufficientFundsTransaction(TypedDict, total=False):
    # Description of the transaction
    description: str

    # Transaction memo
    memo: str

class InsufficientFundsTransaction(RequiredInsufficientFundsTransaction, OptionalInsufficientFundsTransaction):
    pass
