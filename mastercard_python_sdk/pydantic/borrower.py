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

from mastercard_python_sdk.pydantic.consumer_info import ConsumerInfo

class Borrower(BaseModel):
    # A customer ID. See Add Customer API for how to create a customer ID.
    customer_id: str = Field(alias='customerId')

    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    consumer_id: str = Field(alias='consumerId')

    # \"primary\" or \"jointBorrower\"
    type: str = Field(alias='type')

    optional_consumer_info: typing.Optional[ConsumerInfo] = Field(None, alias='optionalConsumerInfo')
    class Config:
        arbitrary_types_allowed = True
