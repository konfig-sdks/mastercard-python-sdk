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


class CreatedConsumer(BaseModel):
    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    id: typing.Optional[str] = Field(None, alias='id')

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    created_date: typing.Optional[int] = Field(None, alias='createdDate')

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customer_id: typing.Optional[int] = Field(None, alias='customerId')
    class Config:
        arbitrary_types_allowed = True
