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


class RequiredCustomerAccountMultipleStatement(TypedDict):
    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    asOfDate: int

    # Returns the index of the month for the statement. It may go up to 24 months back. The valid range is 1-24.
    index: str

class OptionalCustomerAccountMultipleStatement(TypedDict, total=False):
    # Date range representing the period for when the statement data is generated.
    description: str

    # An asset ID. Generated by Connect or by using the Store Customer Pay Statement API.
    id: str

    # The date when the statement was generated.
    documentDate: str

    # Error code for  the bank statement not generated
    code: str

    # Error message for the bank statement not generated
    message: str

class CustomerAccountMultipleStatement(RequiredCustomerAccountMultipleStatement, OptionalCustomerAccountMultipleStatement):
    pass