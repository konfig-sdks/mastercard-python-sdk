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


class CustomerUpdate(BaseModel):
    # The first name of the account holder
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # The last name of the account holder
    last_name: typing.Optional[str] = Field(None, alias='lastName')
    class Config:
        arbitrary_types_allowed = True
