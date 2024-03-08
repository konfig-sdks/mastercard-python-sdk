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

from mastercard_python_sdk.pydantic.customer import Customer

class Customers(BaseModel):
    # The number of results returned
    displaying: int = Field(alias='displaying')

    # If the value of `moreAvailable` is \"true\", you can retrieve the next page of results by increasing the value of the start parameter in your next request:\"...&start=6&limit=5\"
    more_available: bool = Field(alias='moreAvailable')

    # A list of customer records
    customers: typing.List[Customer] = Field(alias='customers')

    # The total number of results matching search criteria
    found: typing.Optional[int] = Field(None, alias='found')
    class Config:
        arbitrary_types_allowed = True
