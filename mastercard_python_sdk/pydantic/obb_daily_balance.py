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


class ObbDailyBalance(BaseModel):
    # Date of balance information
    date: str = Field(alias='date')

    # Day of the week for which balance information available
    day_of_week: str = Field(alias='dayOfWeek')

    # End of day balance
    ending_balance: typing.Union[int, float] = Field(alias='endingBalance')
    class Config:
        arbitrary_types_allowed = True
