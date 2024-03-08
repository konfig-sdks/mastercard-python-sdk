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


class ObbDateRangeAndAmount(BaseModel):
    # Period represented by this metric
    period: str = Field(alias='period')

    # Begin date of the period being reported
    period_begin_date: str = Field(alias='periodBeginDate')

    # End date of the period being reported
    period_end_date: str = Field(alias='periodEndDate')

    # Metric value for the given period
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')
    class Config:
        arbitrary_types_allowed = True
