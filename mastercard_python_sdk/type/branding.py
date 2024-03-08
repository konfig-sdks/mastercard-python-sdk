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


class RequiredBranding(TypedDict):
    pass

class OptionalBranding(TypedDict, total=False):
    # File path of the institution's logo. For white backgrounds designed at 375 x 72, has built in spacing around it to normalize brand sizing.
    logo: str

    # File path of the institution's alternate logo. For colored backgrounds designed at 375 x 72 has built in spacing around it to normalize brand sizing.
    alternateLogo: str

    # File path of the institution's icon. For search results designed at 40 x 40.
    icon: str

    # Hex code for the institution's primary color
    primaryColor: str

    # File path of institution name logo. For popular banks designed at 160 x 72.
    tile: str

class Branding(RequiredBranding, OptionalBranding):
    pass
