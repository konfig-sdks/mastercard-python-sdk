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


class RequiredDeduction(TypedDict):
    pass

class OptionalDeduction(TypedDict, total=False):
    # The deduction line's deduction type description
    description: str

    # The normalized category of the deductions in the format [type][number]. The number is the will be the iterating number of the type's occurrence starting at one.
    name: str

    # The amount for the deduction line deducted from employee's pay for the specified pay period
    amountCurrent: typing.Union[int, float]

    # The amount for the deduction line being deducted from the employee's pay for the current pay year
    amountYTD: typing.Union[int, float]

    # Categorization based on the deduction line's description
    type: str

class Deduction(RequiredDeduction, OptionalDeduction):
    pass
