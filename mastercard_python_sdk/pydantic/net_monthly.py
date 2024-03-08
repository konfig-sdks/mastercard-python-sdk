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


class NetMonthly(BaseModel):
    # Timestamp for the first day of this month
    month: int = Field(alias='month')

    # Total income during the given month, across all income streams
    net: typing.Union[int, float] = Field(alias='net')
    class Config:
        arbitrary_types_allowed = True
