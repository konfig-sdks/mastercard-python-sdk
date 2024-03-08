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

from mastercard_python_sdk.pydantic.transaction import Transaction

class Transactions(BaseModel):
    # The total number of results matching search criteria
    found: int = Field(alias='found')

    # The number of results returned
    displaying: int = Field(alias='displaying')

    # If the value of `moreAvailable` is \"true\", you can retrieve the next page of results by increasing the value of the start parameter in your next request:\"...&start=6&limit=5\"
    more_available: bool = Field(alias='moreAvailable')

    # Value of the `fromDate` request parameter that generated this response
    from_date: int = Field(alias='fromDate')

    # Value of the `toDate` request parameter that generated this response
    to_date: int = Field(alias='toDate')

    # Value of the sort request parameter that generated this response
    sort: str = Field(alias='sort')

    # The array of transactions
    transactions: typing.List[Transaction] = Field(alias='transactions')
    class Config:
        arbitrary_types_allowed = True
