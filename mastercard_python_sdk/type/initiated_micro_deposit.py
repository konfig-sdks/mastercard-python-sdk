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


class RequiredInitiatedMicroDeposit(TypedDict):
    pass

class OptionalInitiatedMicroDeposit(TypedDict, total=False):
    # An account ID
    accountId: str

    # Micro entries successful initiation status
    status: str

    # Count of micro entries
    depositCount: int

    # Micro entries successful initiation description
    statusDescription: str

class InitiatedMicroDeposit(RequiredInitiatedMicroDeposit, OptionalInitiatedMicroDeposit):
    pass
