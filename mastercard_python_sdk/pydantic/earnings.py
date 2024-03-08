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


class Earnings(BaseModel):
    # Categorization of the earnings:  * `base`  * `bonus`  * `overtime`  * `commission`  * `tips`  * `other` 
    type: str = Field(alias='type')

    # Earnings amount for each earning type
    amount: typing.Union[int, float] = Field(alias='amount')

    # Where available, the employer description of earnings on the paycheck
    name: typing.Optional[str] = Field(None, alias='name')

    # Rate of pay
    rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='rate')

    # Earnings YTD amount if available
    amount_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='amountYTD')
    class Config:
        arbitrary_types_allowed = True
