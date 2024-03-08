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


class RequiredACHDetails(TypedDict):
    # The routing number of the financial institution for specific customer account
    routingNumber: str

    # The account number for initiating ACH transfers for this account
    realAccountNumber: str

class OptionalACHDetails(TypedDict, total=False):
    pass

class ACHDetails(RequiredACHDetails, OptionalACHDetails):
    pass
