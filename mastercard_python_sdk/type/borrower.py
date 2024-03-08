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

from mastercard_python_sdk.type.consumer_info import ConsumerInfo

class RequiredBorrower(TypedDict):
    # A customer ID. See Add Customer API for how to create a customer ID.
    customerId: str

    # A consumer ID. See Create Consumer API for how to create a consumer ID.
    consumerId: str

    # \"primary\" or \"jointBorrower\"
    type: str

class OptionalBorrower(TypedDict, total=False):
    optionalConsumerInfo: ConsumerInfo

class Borrower(RequiredBorrower, OptionalBorrower):
    pass
