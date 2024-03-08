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

class NewConsumer(BaseModel):
    # The first name of the account holder
    first_name: str = Field(alias='firstName')

    # The last name of the account holder
    last_name: str = Field(alias='lastName')

    # A street address
    address: str = Field(alias='address')

    # City
    city: str = Field(alias='city')

    # State
    state: str = Field(alias='state')

    # A ZIP code
    zip: str = Field(alias='zip')

    # A phone number (max length 15).
    phone: str = Field(alias='phone')

    # A full SSN with or without hyphens
    ssn: str = Field(alias='ssn')

    birthday: Birthday = Field(alias='birthday')

    # An email address
    email: typing.Optional[str] = Field(None, alias='email')

    # A generational or academic suffix
    suffix: typing.Optional[str] = Field(None, alias='suffix')
    class Config:
        arbitrary_types_allowed = True
