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


class RequiredAccountOwnerEmail(TypedDict):
    pass

class OptionalAccountOwnerEmail(TypedDict, total=False):
    # The email is primary.
    isPrimary: bool

    # An email address
    email: str

    # The account owner's email type.  * \"Personal\"  * \"Business\"
    emailType: str

class AccountOwnerEmail(RequiredAccountOwnerEmail, OptionalAccountOwnerEmail):
    pass
