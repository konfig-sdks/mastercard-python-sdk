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


class Birthday(BaseModel):
    # The birthday 4-digit year
    year: typing.Optional[int] = Field(None, alias='year')

    # The birthday 2-digit month (1 is January)
    month: typing.Optional[int] = Field(None, alias='month')

    # The birthday 2-digit day-of-month
    day_of_month: typing.Optional[int] = Field(None, alias='dayOfMonth')
    class Config:
        arbitrary_types_allowed = True
