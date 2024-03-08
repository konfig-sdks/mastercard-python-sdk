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


class RequiredEarnings(TypedDict):
    # Categorization of the earnings:  * `base`  * `bonus`  * `overtime`  * `commission`  * `tips`  * `other` 
    type: str

    # Earnings amount for each earning type
    amount: typing.Union[int, float]

class OptionalEarnings(TypedDict, total=False):
    # Where available, the employer description of earnings on the paycheck
    name: str

    # Rate of pay
    rate: typing.Union[int, float]

    # Earnings YTD amount if available
    amountYTD: typing.Union[int, float]

class Earnings(RequiredEarnings, OptionalEarnings):
    pass
