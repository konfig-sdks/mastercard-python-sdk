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

from mastercard_python_sdk.pydantic.birthday import Birthday

class ConsumerUpdate(BaseModel):
    # The first name of the account holder
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # The last name of the account holder
    last_name: typing.Optional[str] = Field(None, alias='lastName')

    # A street address
    address: typing.Optional[str] = Field(None, alias='address')

    # City
    city: typing.Optional[str] = Field(None, alias='city')

    # State
    state: typing.Optional[str] = Field(None, alias='state')

    # A ZIP code
    zip: typing.Optional[str] = Field(None, alias='zip')

    # A phone number (max length 15).
    phone: typing.Optional[str] = Field(None, alias='phone')

    # A full SSN with or without hyphens
    ssn: typing.Optional[str] = Field(None, alias='ssn')

    birthday: typing.Optional[Birthday] = Field(None, alias='birthday')

    # An email address
    email: typing.Optional[str] = Field(None, alias='email')

    # A generational or academic suffix
    suffix: typing.Optional[str] = Field(None, alias='suffix')
    class Config:
        arbitrary_types_allowed = True
