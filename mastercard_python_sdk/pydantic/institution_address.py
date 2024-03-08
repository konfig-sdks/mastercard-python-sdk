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


class InstitutionAddress(BaseModel):
    # City
    city: typing.Optional[str] = Field(None, alias='city')

    # State
    state: typing.Optional[str] = Field(None, alias='state')

    # Country code is Iso3166-1 Alpha-2 code and Alpha 3 standard (max length 3).
    country: typing.Optional[str] = Field(None, alias='country')

    # A ZIP code
    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    # Address line 1
    address_line1: typing.Optional[str] = Field(None, alias='addressLine1')

    # Address line 2
    address_line2: typing.Optional[str] = Field(None, alias='addressLine2')
    class Config:
        arbitrary_types_allowed = True
