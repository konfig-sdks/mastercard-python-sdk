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


class RequiredApplication(TypedDict):
    # A short description of the app. This will be visible to end users in the FI interface.
    appDescription: str

    # The name of the application assigned to the customer
    appName: str

    # An URL for the app. This will be visible to end users in the FI interface.
    appUrl: str

    # Address line 1
    ownerAddressLine1: str

    # Address line 2
    ownerAddressLine2: str

    # City for the business entity that owns the app. Information for registration purposes only and not given to the end user.
    ownerCity: str

    # Country for the  business entity that owns the app. Information for registration purposes only and not given to the end user.
    ownerCountry: str

    # Business name for the business entity that owns the app. Information for registration purposes only and not given to the end user.
    ownerName: str

    # Zip code for the business entity that owns the app. Information for registration purposes only and not given to the end user.
    ownerPostalCode: str

    # State for the business entity that owns the app. Information for registration purposes only and not given to the end user.
    ownerState: str

    # An app logo passed as a Base64 encoded image (1:1 SVG file, must be less than 50KB)
    image: str

class OptionalApplication(TypedDict, total=False):
    pass

class Application(RequiredApplication, OptionalApplication):
    pass
