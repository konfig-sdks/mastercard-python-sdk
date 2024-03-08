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


class RequiredAccountOwner(TypedDict):
    # The name of the account owner. Can be multiple account owners in one string. This is how the source data is returned from the institution.
    ownerName: str

    # A street address
    ownerAddress: str

class OptionalAccountOwner(TypedDict, total=False):
    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    asOfDate: int

class AccountOwner(RequiredAccountOwner, OptionalAccountOwner):
    pass
