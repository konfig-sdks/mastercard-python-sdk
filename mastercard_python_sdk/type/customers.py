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

from mastercard_python_sdk.type.customer import Customer

class RequiredCustomers(TypedDict):
    # The number of results returned
    displaying: int

    # If the value of `moreAvailable` is \"true\", you can retrieve the next page of results by increasing the value of the start parameter in your next request:\"...&start=6&limit=5\"
    moreAvailable: bool

    # A list of customer records
    customers: typing.List[Customer]

class OptionalCustomers(TypedDict, total=False):
    # The total number of results matching search criteria
    found: int

class Customers(RequiredCustomers, OptionalCustomers):
    pass
