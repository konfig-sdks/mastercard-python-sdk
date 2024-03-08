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


class AccountOwnerAddress(BaseModel):
    # A street address
    owner_address: typing.Optional[str] = Field(None, alias='ownerAddress')

    # The type of address location: * \"Business\" * \"Home\" * \"Mailing\"
    type: typing.Optional[str] = Field(None, alias='type')

    # Address line 1
    line1: typing.Optional[str] = Field(None, alias='line1')

    # Address line 2
    line2: typing.Optional[str] = Field(None, alias='line2')

    # Address line 3
    line3: typing.Optional[str] = Field(None, alias='line3')

    # City
    city: typing.Optional[str] = Field(None, alias='city')

    # State
    state: typing.Optional[str] = Field(None, alias='state')

    # A ZIP code
    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    # Country code is Iso3166-1 Alpha-2 code and Alpha 3 standard (max length 3).
    country: typing.Optional[str] = Field(None, alias='country')
    class Config:
        arbitrary_types_allowed = True
