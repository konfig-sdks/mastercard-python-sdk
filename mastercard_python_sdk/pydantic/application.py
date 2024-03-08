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
from pydantic import BaseModel, Field, RootModel


class Application(BaseModel):
    # A short description of the app. This will be visible to end users in the FI interface.
    app_description: str = Field(alias='appDescription')

    # The name of the application assigned to the customer
    app_name: str = Field(alias='appName')

    # An URL for the app. This will be visible to end users in the FI interface.
    app_url: str = Field(alias='appUrl')

    # Address line 1
    owner_address_line1: str = Field(alias='ownerAddressLine1')

    # Address line 2
    owner_address_line2: str = Field(alias='ownerAddressLine2')

    # City for the business entity that owns the app. Information for registration purposes only and not given to the end user.
    owner_city: str = Field(alias='ownerCity')

    # Country for the  business entity that owns the app. Information for registration purposes only and not given to the end user.
    owner_country: str = Field(alias='ownerCountry')

    # Business name for the business entity that owns the app. Information for registration purposes only and not given to the end user.
    owner_name: str = Field(alias='ownerName')

    # Zip code for the business entity that owns the app. Information for registration purposes only and not given to the end user.
    owner_postal_code: str = Field(alias='ownerPostalCode')

    # State for the business entity that owns the app. Information for registration purposes only and not given to the end user.
    owner_state: str = Field(alias='ownerState')

    # An app logo passed as a Base64 encoded image (1:1 SVG file, must be less than 50KB)
    image: str = Field(alias='image')
    class Config:
        arbitrary_types_allowed = True
