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


class RequiredAccountOwnerPhone(TypedDict):
    pass

class OptionalAccountOwnerPhone(TypedDict, total=False):
    # The account owner's phone type:  * \"HOME\"  * \"BUSINESS\"  * \"CELL\"  * \"FAX\"
    type: str

    # Country calling code of the phone number as defined by ITU-T E.123 and E.164 international standards (max length 3)\".
    country: str

    # A phone number (max length 15).
    phone: str

class AccountOwnerPhone(RequiredAccountOwnerPhone, OptionalAccountOwnerPhone):
    pass
