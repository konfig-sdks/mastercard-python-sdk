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


class RequiredCreatedTestTxPushTransaction(TypedDict):
    # A transaction ID
    id: int

    # A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/).
    createdDate: int

class OptionalCreatedTestTxPushTransaction(TypedDict, total=False):
    pass

class CreatedTestTxPushTransaction(RequiredCreatedTestTxPushTransaction, OptionalCreatedTestTxPushTransaction):
    pass
