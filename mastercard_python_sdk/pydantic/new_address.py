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

from mastercard_python_sdk.pydantic.country_code import CountryCode

class NewAddress(BaseModel):
    # Address line 1
    address_line1: typing.Optional[str] = Field(None, alias='addressLine1')

    # Address line 2
    address_line2: typing.Optional[str] = Field(None, alias='addressLine2')

    # City
    city: typing.Optional[str] = Field(None, alias='city')

    # State
    state: typing.Optional[str] = Field(None, alias='state')

    country: typing.Optional[CountryCode] = Field(None, alias='country')

    # A ZIP code
    postal_code: typing.Optional[str] = Field(None, alias='postalCode')
    class Config:
        arbitrary_types_allowed = True
