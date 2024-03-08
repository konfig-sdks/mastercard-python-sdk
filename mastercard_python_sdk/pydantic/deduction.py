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


class Deduction(BaseModel):
    # The deduction line's deduction type description
    description: typing.Optional[str] = Field(None, alias='description')

    # The normalized category of the deductions in the format [type][number]. The number is the will be the iterating number of the type's occurrence starting at one.
    name: typing.Optional[str] = Field(None, alias='name')

    # The amount for the deduction line deducted from employee's pay for the specified pay period
    amount_current: typing.Optional[typing.Union[int, float]] = Field(None, alias='amountCurrent')

    # The amount for the deduction line being deducted from the employee's pay for the current pay year
    amount_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='amountYTD')

    # Categorization based on the deduction line's description
    type: typing.Optional[str] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
