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


class RequiredAccountOwnerAddress(TypedDict):
    pass

class OptionalAccountOwnerAddress(TypedDict, total=False):
    # A street address
    ownerAddress: str

    # The type of address location: * \"Business\" * \"Home\" * \"Mailing\"
    type: str

    # Address line 1
    line1: str

    # Address line 2
    line2: str

    # Address line 3
    line3: str

    # City
    city: str

    # State
    state: str

    # A ZIP code
    postalCode: str

    # Country code is Iso3166-1 Alpha-2 code and Alpha 3 standard (max length 3).
    country: str

class AccountOwnerAddress(RequiredAccountOwnerAddress, OptionalAccountOwnerAddress):
    pass
