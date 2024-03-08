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

class Consumer(BaseModel):
    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    id: str = Field(alias='id')

    # The first name of the account holder
    first_name: str = Field(alias='firstName')

    # The last name of the account holder
    last_name: str = Field(alias='lastName')

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customer_id: int = Field(alias='customerId')

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

    # Last 4 digits of a SSN
    ssn: str = Field(alias='ssn')

    birthday: Birthday = Field(alias='birthday')

    # An email address
    email: str = Field(alias='email')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    created_date: int = Field(alias='createdDate')

    # A generational or academic suffix
    suffix: typing.Optional[str] = Field(None, alias='suffix')
    class Config:
        arbitrary_types_allowed = True
