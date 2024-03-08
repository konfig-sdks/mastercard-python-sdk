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


class AccountOwner(BaseModel):
    # The name of the account owner. Can be multiple account owners in one string. This is how the source data is returned from the institution.
    owner_name: str = Field(alias='ownerName')

    # A street address
    owner_address: str = Field(alias='ownerAddress')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    as_of_date: typing.Optional[int] = Field(None, alias='asOfDate')
    class Config:
        arbitrary_types_allowed = True
