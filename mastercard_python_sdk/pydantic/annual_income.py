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


class AnnualIncome(BaseModel):
    # The year for the amounts given in YTD totals for an employer
    year: str = Field(alias='year')

    # Year to date (YTD) gross pay amount for the indicated year
    gross_pay_amount_y_t_d: typing.Union[int, float] = Field(alias='grossPayAmountYTD')

    # Year to date (YTD) net pay amount for the indicated year
    net_pay_amount_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='netPayAmountYTD')

    # Year to date (YTD) base pay amount for the year indicated
    base_pay_amount_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='basePayAmountYTD')

    # Year to date (YTD) overtime pay amount for the year indicated
    overtime_pay_amount_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='overtimePayAmountYTD')

    # Year to date (YTD) other pay amount for the indicated year. Other pay is pay that is not categorized into one of the other categories.
    other_pay_amount_y_t_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='otherPayAmountYTD')

    # Year to date (YTD) commission pay amount for the indicated year
    commission_pay_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='commissionPayAmount')
    class Config:
        arbitrary_types_allowed = True
