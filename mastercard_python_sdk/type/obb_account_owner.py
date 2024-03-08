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


class RequiredObbAccountOwner(TypedDict):
    # Address of the owner on record for the account
    address: str

    # Name of the owner on record for the account
    name: str

class OptionalObbAccountOwner(TypedDict, total=False):
    pass

class ObbAccountOwner(RequiredObbAccountOwner, OptionalObbAccountOwner):
    pass
