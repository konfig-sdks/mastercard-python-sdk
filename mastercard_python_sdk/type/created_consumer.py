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


class RequiredCreatedConsumer(TypedDict):
    pass

class OptionalCreatedConsumer(TypedDict, total=False):
    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    id: str

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    createdDate: int

    # A customer ID represented as a number. See Add Customer API for how to create a customer ID.
    customerId: int

class CreatedConsumer(RequiredCreatedConsumer, OptionalCreatedConsumer):
    pass
