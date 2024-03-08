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


class RequiredInstitutionAddress(TypedDict):
    pass

class OptionalInstitutionAddress(TypedDict, total=False):
    # City
    city: str

    # State
    state: str

    # Country code is Iso3166-1 Alpha-2 code and Alpha 3 standard (max length 3).
    country: str

    # A ZIP code
    postalCode: str

    # Address line 1
    addressLine1: str

    # Address line 2
    addressLine2: str

class InstitutionAddress(RequiredInstitutionAddress, OptionalInstitutionAddress):
    pass
