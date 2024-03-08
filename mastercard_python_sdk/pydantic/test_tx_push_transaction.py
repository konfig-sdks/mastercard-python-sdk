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


class TestTxPushTransaction(BaseModel):
    # The description of the transaction
    description: str = Field(alias='description')

    # The amount of the transaction
    amount: typing.Union[int, float] = Field(alias='amount')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    transaction_date: int = Field(alias='transactionDate')

    # \"active\" or \"pending\" (optional)
    status: typing.Optional[str] = Field(None, alias='status')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    posted_date: typing.Optional[int] = Field(None, alias='postedDate')
    class Config:
        arbitrary_types_allowed = True
