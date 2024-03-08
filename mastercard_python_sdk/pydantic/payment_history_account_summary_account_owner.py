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


class PaymentHistoryAccountSummaryAccountOwner(BaseModel):
    # The full name of the account owner. Multiple account owners are returned in one string per the source data from the institution.
    name: str = Field(alias='name')

    # A street address
    address: str = Field(alias='address')

    # City
    city: typing.Optional[str] = Field(None, alias='city')

    # State
    state: typing.Optional[str] = Field(None, alias='state')

    # A ZIP code
    zip: typing.Optional[str] = Field(None, alias='zip')
    class Config:
        arbitrary_types_allowed = True
